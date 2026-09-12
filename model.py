import numpy as np
from utils import get_logger, SIMILARITY_THRESHOLD
from features import TFIDFExtractor
from data_loader import DataLoader

log = get_logger("ModelPipeline")

# ==========================================
# Mathematical calculation module for vector similarity
# ==========================================
class SimilarityEngine:
    def cosine_similarity(self, vec1, vec2):
        if np.all(vec1 == 0) or np.all(vec2 == 0):
            log.warning("One of the provided vectors contains only zeros.")
            return 0.0
        # Calculate Cosine Similarity using NumPy operations
        dot_product = np.dot(vec1, vec2)
        norm_a = np.linalg.norm(vec1)
        norm_b = np.linalg.norm(vec2)
        if norm_a == 0 or norm_b == 0:
            return 0.0
        sim = dot_product / (norm_a * norm_b)
        sim = max(0.0, min(1.0, float(sim)))
        log.debug(f"Calculated Cosine Similarity: {sim}")
        return sim

# ==========================================
# Output and evaluation generation module
# ==========================================
class MatchEvaluator:
    def __init__(self, engine):
        self.engine = engine
        
    def evaluate(self, jd_vec, resume_vec, extractor):
        log.info("Evaluating resume compatibility...")
        score = self.engine.cosine_similarity(jd_vec, resume_vec)
        
        missing_skills = []
        feature_names = extractor.get_feature_names()
        
        # Identify high-value keywords missing from the resume vector
        for i in range(len(feature_names)):
            word = feature_names[i]
            if jd_vec[i] > 0.05 and resume_vec[i] == 0:
                missing_skills.append(word)
                
        # Sort missing keywords by their importance in the job description
        missing_skills.sort(key=lambda w: jd_vec[extractor.vocab[w]], reverse=True)
        missing_skills = missing_skills[:10]
        
        return {
            "score": score,
            "is_match": score >= SIMILARITY_THRESHOLD,
            "missing_keywords": missing_skills
        }
        
    def generate_report(self, results):
        print("="*40)
        print("RESUME ATS ANALYSIS REPORT")
        print("="*40)
        score_pct = round(results['score'] * 100, 2)
        print(f"Calculated Match Score: {score_pct}%")
        
        if results['is_match']:
            print("Evaluation: STRONG MATCH. Candidate meets ATS threshold.")
        else:
            print(f"Evaluation: WEAK MATCH. Required threshold is {SIMILARITY_THRESHOLD*100}%.")
            
        print("\nCritical Missing Keywords Detected:")
        if len(results['missing_keywords']) == 0:
            print("- No significant missing keywords detected.")
        else:
            for w in results['missing_keywords']:
                print(f"- {w}")
        print("="*40)

# ==========================================
# Main execution pipeline integrating all modules
# ==========================================
class ATSPipeline:
    def __init__(self):
        self.loader = DataLoader()
        self.engine = SimilarityEngine()
        self.evaluator = MatchEvaluator(self.engine)
        
    def run(self, jd_path, resume_path):
        log.info(f"Initiating pipeline processing for {jd_path} and {resume_path}")
        
        jd_text = self.loader.load_document(jd_path)
        resume_text = self.loader.load_document(resume_path)
        
        if not jd_text or not resume_text:
            log.error("Document extraction failed. Terminating pipeline.")
            return
            
        extractor = TFIDFExtractor()
        corpus = [jd_text, resume_text]
        extractor.fit(corpus)
        
        # Transform extracted text into TF-IDF vectors
        jd_vec = extractor.transform(jd_text)
        resume_vec = extractor.transform(resume_text)
        
        # Evaluate compatibility and generate terminal report
        results = self.evaluator.evaluate(jd_vec, resume_vec, extractor)
        self.evaluator.generate_report(results)

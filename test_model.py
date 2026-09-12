import unittest
import numpy as np
from features import TFIDFExtractor
from model import SimilarityEngine

class TestResumeAnalyzer(unittest.TestCase):
    def test_cosine_similarity(self):
        engine = SimilarityEngine()
        vec1 = np.array([1, 0, 1])
        vec2 = np.array([1, 1, 0])
        sim = engine.cosine_similarity(vec1, vec2)
        self.assertAlmostEqual(sim, 0.5)

    def test_zero_vector_similarity(self):
        engine = SimilarityEngine()
        vec1 = np.array([0, 0, 0])
        vec2 = np.array([1, 1, 1])
        sim = engine.cosine_similarity(vec1, vec2)
        self.assertEqual(sim, 0.0)

    def test_tfidf_extractor(self):
        extractor = TFIDFExtractor()
        corpus = ["python java sql", "python java"]
        extractor.fit(corpus)
        vec1 = extractor.transform(corpus[0])
        vec2 = extractor.transform(corpus[1])
        self.assertEqual(len(vec1), len(extractor.vocab))
        self.assertTrue(np.any(vec1 > 0))
        self.assertTrue(np.any(vec2 > 0))

if __name__ == '__main__':
    unittest.main()

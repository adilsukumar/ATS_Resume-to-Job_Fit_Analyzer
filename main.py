import argparse
import sys
from model import ATSPipeline
from utils import get_logger

# Initialize the logger for debugging and monitoring
log = get_logger("Main")

def main():
    parser = argparse.ArgumentParser(description="AI Resume-to-Job Fit Analyzer")
    
    # Define required command-line arguments for file inputs
    parser.add_argument("--jd", type=str, required=True, help="Path to the Job Description (txt or pdf)")
    parser.add_argument("--resume", type=str, required=True, help="Path to the Resume (txt or pdf)")
    
    args = parser.parse_args()
    
    try:
        # Instantiate and execute the main pipeline
        pipeline = ATSPipeline()
        pipeline.run(args.jd, args.resume)
    except Exception as e:
        log.error(f"A fatal error occurred during execution: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Validate arguments before execution
    if len(sys.argv) == 1:
        print("Error: Please provide both --jd and --resume arguments.")
        sys.exit(1)
        
    main()

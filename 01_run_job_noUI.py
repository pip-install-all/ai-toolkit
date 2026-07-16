import os
import sys
from pathlib import Path
import uuid
import argparse

# Get the directory where this script is located
script_dir = Path(__file__).parent.absolute()
# Add the ai-toolkit directory to Python path
toolkit_path = script_dir / "ai-toolkit"
sys.path.insert(0, str(toolkit_path))

# Now import the toolkit
from toolkit.job import get_job


def load_and_run_job(config_path):
    print(f"Loading and running job from {config_path}")

    # Set required environment variable
    os.environ["AITK_JOB_ID"] = str(uuid.uuid4())

    job = get_job(config_path)
    try:
        job.run()
        print("✅ Job completed successfully.")
    except Exception as e:
        print(f"❌ Job failed: {e}")
        raise
    finally:
        job.cleanup()


def main():
    parser = argparse.ArgumentParser(description='Run AI toolkit jobs')
    parser.add_argument('config_path', nargs='?', default="0_rub/configs_tests/r_train_lora_chroma_24gb.yaml",
                        help='Path to the YAML config file')

    args = parser.parse_args()

    # Validate config file exists
    if not os.path.exists(args.config_path):
        raise FileNotFoundError(f"Config file not found: {args.config_path}")

    load_and_run_job(args.config_path)


# --- RUN THE JOB ---
if __name__ == "__main__":
    main()

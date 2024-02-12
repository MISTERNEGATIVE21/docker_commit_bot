import os
from datetime import datetime, timedelta
from github import Github
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

# Get environment variables
github_username = os.getenv("GITHUB_USERNAME")
github_token = os.getenv("GITHUB_TOKEN")
repo_owner = os.getenv("REPO_OWNER")
repo_name = os.getenv("REPO_NAME")
times_to_execute = int(os.getenv("TIMES_TO_EXECUTE", 1))  # Default to 1 if not set

# Ensure that all required environment variables are present
if None in (github_username, github_token, repo_owner, repo_name):
    print("Please set all required environment variables.")
    exit(1)

# Calculate the interval in seconds between each execution
interval_seconds = int((24 * 60 * 60) / times_to_execute)

# Create a GitHub instance using your token
g = Github(github_token)

# Get the repository
repo = g.get_user(repo_owner).get_repo(repo_name)

# Perform the code execution periodically
for _ in range(times_to_execute):
    # Create a new file with the current date and time as content
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_content = f"Commit on {current_time}"
    file_path = f"commits/{current_time}.txt"

    # Commit the file to the repository
    try:
        contents = repo.get_contents(file_path)
    except:
        contents = None

    if contents is None:
        repo.create_file(file_path, f"Commit on {current_time}", file_content, branch="main")
        print(f"Committed changes for {current_time}")
    else:
        print(f"Changes already committed for {current_time}")

    # Sleep for the calculated interval
    time.sleep(interval_seconds)

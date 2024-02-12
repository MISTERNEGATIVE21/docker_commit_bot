# Dockerized Git Commit Bot
Dockerised Git Commit bot : - Commit a Day Keeps your Tensions Away !

![output (2)](https://github.com/MISTERNEGATIVE21/docker_commit_bot/assets/51168229/88187ba4-e695-4d96-b3ef-fd0dccb2b225)

#### Description
A Git commit bot that automatically commits every day.

## Usage Instructions
Follow these steps to use the Dockerized Git Commit Bot.

1. Clone the repository.
2. Build the Docker image.
3. Run the Docker container.

## GitHub Token
To use this bot, obtain a GitHub Personal Access Token with the necessary scopes.

1. Go to [GitHub](https://github.com/).
2. Click on your profile picture > Settings > Developer settings > Personal access tokens.
3. Generate a token with `repo` and `user` scopes with expiry time.

<img width="993" alt="image" src="https://github.com/MISTERNEGATIVE21/docker_commit_bot/assets/51168229/db47a3f0-c864-4b40-9a68-226d69bdcc8b">

## Setup Steps
1. **Go to GitHub.**
   - Visit [GitHub](https://github.com/).
  
2. **Click on the "+" sign in the top right and select "New repository."**
   - Click on the "+" icon located in the top right corner of the GitHub page.
   - Select "New repository."

3. **Provide a name, select "Private," and add a meaningful description.**
   - Fill in a name for your repository.
   - Choose "Private" as the repository visibility.
   - Add a meaningful description for your repository.

4. **Initialize the repository with a README or add a .gitignore file if needed.**
   - Optionally, you can choose to initialize the repository with a README file.
   - If necessary, select a .gitignore file based on your project requirements.

5. **Save the GitHub repository URL and customize the .env file:**
   - Save the URL of your private repository.
   - Customize the `.env` file or modify Docker Compose YAML to set the GitHub repository URL and other variables.

6. **Build the Docker image:**
   - Build the Docker image using the following command:
     ```bash
     docker build -t git-commit-bot .
     ```
# Shortcut Method: Deploy Docker Compose with Variable Edits

1. **Copy docker-compose.yaml file:**

2. **Edit .env File**

Follow these steps to customize the application configuration by editing the `.env` file:

1. ***Open the .env File:***
   - Using a text editor, open the `.env` file in the project directory.

2. ***Modify the Variables:***
   - Update the following variables based on your configuration:
     - `GITHUB_USERNAME=your-github-username`
     - `GITHUB_TOKEN=your-github-token`
     - `REPO_OWNER=your-github-username`
     - `REPO_NAME=your-repo-name`
     - `TIMES_TO_EXECUTE=(keep it between4-5)`
Save the changes after modifying the variables to tailor the application to your GitHub environment.

**Advice:**
![312d9804-161d-41fd-8b0a-51980fd35398](https://github.com/MISTERNEGATIVE21/docker_commit_bot/assets/51168229/b5dc29df-5786-4957-b88d-216197c80531)

This project is meant to be a fun and light-hearted experiment. Please use it responsibly and avoid any misuse of the GitHub platform. Excessive or inappropriate use of automated commit tools can violate GitHub's terms of service.

Remember to respect the community guidelines and terms set by GitHub. Use this tool in a positive and constructive manner, and always be mindful of ethical considerations. Let's keep the coding community enjoyable for everyone!
Thank you for using our Dockerized Git Commit Bot! If you have any questions or need assistance, feel free to reach out. Happy coding!

# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set default values for build-time arguments
ARG GITHUB_USERNAME_ARG=default_username
ARG GITHUB_TOKEN_ARG=default_access_token
ARG REPO_OWNER_ARG=default_owner_username
ARG REPO_NAME_ARG=default_repository_name

# Set environment variables for runtime
ENV GITHUB_USERNAME=$GITHUB_USERNAME_ARG
ENV GITHUB_TOKEN=$GITHUB_TOKEN_ARG
ENV REPO_OWNER=$REPO_OWNER_ARG
ENV REPO_NAME=$REPO_NAME_ARG

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org requests PyGithub python-dotenv

# Make port 80 available to the world outside this container
# EXPOSE 80

# Run app.py when the container launches
CMD ["python", "commit_bot.py"]

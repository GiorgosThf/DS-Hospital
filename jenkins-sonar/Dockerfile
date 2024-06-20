# Use the official Jenkins LTS image from Docker Hub
FROM jenkins/jenkins:lts

# Switch to root user for installation
USER root

# Install necessary tools and dependencies

# Update package lists and install Python 3 with pip
RUN apt-get update && apt-get install -y python3 python3-venv


# Switch back to Jenkins user
USER jenkins
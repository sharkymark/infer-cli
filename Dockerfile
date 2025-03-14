# Define the argument before its first use
FROM python:3.9-slim

# get utilities in the container
RUN apt-get update && apt-get install -y curl procps ssh git net-tools htop

# Install pip dependencies
RUN pip install --no-cache-dir --upgrade pip

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
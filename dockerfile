# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install dependencies for building Python packages
RUN apt-get update && apt-get install -y \
    git \
    wget \
    cmake \
    build-essential

# Install Git LFS
RUN wget https://packagecloud.io/github/git-lfs/gpgkey -O - | apt-key add - \
    && echo "deb https://packagecloud.io/github/git-lfs/debian/ buster main" | tee /etc/apt/sources.list.d/git-lfs.list \
    && apt-get update \
    && apt-get install -y git-lfs \
    && git lfs install

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variables
ENV UVICORN_HOST=0.0.0.0
ENV UVICORN_PORT=8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

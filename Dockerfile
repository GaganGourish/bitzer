# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
# Uncomment the next line if you have external dependencies in a requirements.txt file
#RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
# Uncomment and modify the next line if you need to set environment variables
# ENV NAME World

# Run your Python script when the container launches
ENTRYPOINT ["python3", "pet.py"]
CMD []
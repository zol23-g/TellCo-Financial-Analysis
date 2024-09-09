# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /

# Copy the requirements.txt into the image
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000 for the MLflow server
EXPOSE 5000

# Start MLflow tracking server on container start
CMD ["mlflow", "ui", "--host", "0.0.0.0"]

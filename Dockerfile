# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose port for MLflow UI (optional)
EXPOSE 5000

# Run the model script (or mlflow ui for tracking)
CMD ["mlflow", "ui"]

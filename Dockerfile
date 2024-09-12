# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Supervisor to manage multiple services
RUN apt-get update && apt-get install -y supervisor

# Copy the Supervisor configuration file into the container
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose the ports for both MLflow (5000) and Streamlit (8501)
EXPOSE 5000 8501

# Start Supervisor to manage both MLflow and Streamlit
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files to container
COPY . .

# Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

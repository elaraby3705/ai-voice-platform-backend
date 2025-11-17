# Step 1: Base image
FROM python:3.12-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy application code
COPY . .

# Step 5: Expose port for Cloud Run
EXPOSE 8080

# Step 6: Default command to run your app
# (replace app:app with your WSGI/ASGI entrypoint)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]

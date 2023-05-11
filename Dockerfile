# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SECRET_KEY = v1sht=unae23=)ujzf5$og%g%5#gyiq^l9okrgsv9t0tsrn0=v
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install project dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Expose the port the Django application will run on
EXPOSE 8000

# Define the command to run when starting the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

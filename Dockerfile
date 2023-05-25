# Use the official Python image as the base image
FROM python:3.11.2

# set working directory
WORKDIR /particle

# Copy the project file to the container
COPY . /particle

# Install dependencies
RUN pip install -r requirements.txt

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:3001"]

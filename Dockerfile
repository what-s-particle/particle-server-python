# Use the official Python image as the base image
FROM python:3.13.0

# set working directory
WORKDIR /particle

# Copy the project file to the container
COPY . /particle

# Install dependencies
RUN pip install -r requirements.txt

EXPOSE 3001

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:3001"]

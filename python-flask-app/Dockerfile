# Base Image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the files
COPY . .

# Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
# For Jenkinsfile all-in-one location updates
RUN pip install --no-cache-dir -r python-flask-app/requirements.txt


# Enviroment setup - by default flask runs on 5000 port, which is not recommended for production
# ENV FLASK_APP=app.py
# For Jenkinsfile all-in-one location updates
ENV FLASK_APP=python-flask-app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=3000

# Run app.py when the container launches
CMD [ "flask", "run" ]
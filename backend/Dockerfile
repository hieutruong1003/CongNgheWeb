# Use an official Python runtime as a parent image
FROM python:3.6.9

RUN apt-get update
RUN apt-get install -y libpq-dev python3-dev build-essential postgresql-server-dev-all

# Set the working directory to /app
WORKDIR /app

COPY requirements.txt /app
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Copy the current directory contents into the container
COPY . /app

#Make port available to the world outside this container 
EXPOSE 8080

# Run app.py when the container launches
CMD ["python","app.py"]
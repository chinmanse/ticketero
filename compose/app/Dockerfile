FROM python:3.11.2

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN apt-get install -y \
    wget vim netcat

# Copy the requirements file into the container
COPY ./compose/app/requirements.txt /tmp/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
  pip install --no-cache-dir -r /tmp/requirements.txt && \
  rm -rf /root/.cache/pip/*

# Copy the startup script into the container
COPY ./compose/app/start.sh /start

# Make the startup script executable
RUN chmod +x /start

# Set the working directory to /app
WORKDIR /app

# Start the app using the startup script
CMD ["/start"]

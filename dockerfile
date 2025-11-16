# The Python Image from the Docker Hub. Using the slim verison to keep the image size small as not to use unnecessary space
FROM python:3.9-slim

# Creates a dictory named App inside the container
WORKDIR /app

# Copies the requirements.txt file into the container and calls WORKDIR so that it's copied into the /app dictory
COPY requirements.txt .

# Copies all files on host machine into the container
COPY . .

# Installs all dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Runs and builds the Image
CMD [ "python", "app.py" ]
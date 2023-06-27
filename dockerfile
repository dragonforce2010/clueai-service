# use official python runtime
from python:3.9-buster

# install the required packages
run apt-get update && apt-get install -y --no-install-recommends ca-certificates

# set the working directory to /app
workdir /app

copy ./requirements.txt ./
run pip install --no-cache-dir -r requirements.txt

# copy the application code to the container
copy . .

env FLASK_APP=app.py

expose 5000

cmd ["flask", "run", "--host=0.0.0.0"]
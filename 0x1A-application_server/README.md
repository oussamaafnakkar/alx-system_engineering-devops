# 0x1A Application Server - Task 0

This project involves setting up development with Python for the AirBnB clone v2 on the web-01 server. The Flask application will be configured to serve its content from the route `/airbnb-onepage/` on port 5000.

## Prerequisites

- Ensure that task #3 of the SSH project is completed for web-01.
- Install the net-tools package on your server:
  ```bash
  sudo apt install -y net-tools
Setup

    Clone the AirBnB_clone_v2 repository on web-01:
    git clone https://github.com/oussamaafnakkar/AirBnB_clone_v2.git
Configure Flask Application:

    Edit the file web_flask/0-hello_route.py to serve content from the route /airbnb-onepage/ on port 5000.

python

# web_flask/0-hello_route.py
from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

Run the Flask App:

bash

python3 -m web_flask.0-hello_route

Example Output:

    You should see output similar to the example provided in the task.
Configure Flask Application:

    Edit the file web_flask/0-hello_route.py to serve content from the route /airbnb-onepage/ on port 5000.

python

# web_flask/0-hello_route.py
from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

Run the Flask App:

bash

python3 -m web_flask.0-hello_route

Example Output:

    You should see output similar to the example provided in the task.

Test with Curl:

    In another terminal window, test the Flask app using curl.

    bash

    curl 127.0.0.1:5000/airbnb-onepage/

    Verify that the response is 'Hello HBNB!'

Commit Changes:

bash

git add web_flask/0-hello_route.py
git commit -m "Configure Flask app to serve content at /airbnb-onepage/"
git push
Test with Curl:

    In another terminal window, test the Flask app using curl.

    bash

    curl 127.0.0.1:5000/airbnb-onepage/

    Verify that the response is 'Hello HBNB!'

Commit Changes:

bash

git add web_flask/0-hello_route.py
git commit -m "Configure Flask app to serve content at /airbnb-onepage/"
git push
Author
OUSSAMA AFNAKKAR

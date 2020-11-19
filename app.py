from flask import Flask
import requests
from datetime import datetime

app = Flask(__name__)


def is_eight():
    return datetime.now().strftime("%H%M") == "0800"


while True:
    if is_eight():
        requests.post("http://localhost:8000/send/email/reminder")


if __name__ == '__main__':
    app.run()

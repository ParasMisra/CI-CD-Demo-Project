from flask import Flask
import logging
import os

app = Flask(__name__)

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route("/")
def home():
    message = "Application started successfully"
    logging.info(message)
    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
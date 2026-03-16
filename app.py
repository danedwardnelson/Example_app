import logging

from flask import Flask, jsonify

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def home():
    try:
        logger.info("Handling request for /")
        return "Internal Tool Running"
    except Exception:
        logger.exception("Error while handling /")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route("/health")
def health():
    logger.info("Handling request for /health")
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    logger.info("Starting Flask app on 0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000)

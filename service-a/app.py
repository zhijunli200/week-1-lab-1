from flask import Flask, request, jsonify
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/sendMessage")
def echo():
    start = time.time()
    message = request.args.get("message")
    if message is None or message == "":
        message = "hello world from service A"
    response = {"message": message}
    logging.info(f'service = A endpoint = /sendMessage status = ok latency_ms = {int((time.time()-start)*1000)}')
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

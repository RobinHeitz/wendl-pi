import RPi.GPIO as GPIO
from flask import Flask, jsonify, render_template

app = Flask("app")

LIGHT_GPIO = 21
LIGHT_ON = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/toggle", methods=["POST"])
def toggle():
    global LIGHT_ON
    LIGHT_ON = not LIGHT_ON
    GPIO.output(21, LIGHT_ON)
    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")

import io
from threading import Condition

import picamera
import RPi.GPIO as GPIO
from flask import Flask, Response, jsonify, render_template

app = Flask("app")

LIGHT_GPIO = 21
LIGHT_ON = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

output = io.BytesIO()
condition = Condition()


class CameraOutput:
    def __init__(self):
        self.frame = None

    def write(self, buf):
        if buf.startswith(b"\xff\xd8"):
            # New frame, store existing one
            self.frame = buf
            with condition:
                condition.notify_all()


camera_output = CameraOutput()


def gen(camera):
    while True:
        with condition:
            condition.wait()
            frame = camera.frame
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/toggle", methods=["POST"])
def toggle():
    global LIGHT_ON
    LIGHT_ON = not LIGHT_ON
    GPIO.output(21, LIGHT_ON)
    return jsonify({"status": "success"})


@app.route("/video_feed")
def video_feed():
    return Response(
        gen(camera_output), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    with picamera.PiCamera(resolution="640x480", framerate=10) as camera:
        camera.start_recording(camera_output, format="mjpeg")
        app.run(debug=True, port=8000, host="0.0.0.0")

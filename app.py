from flask import Flask, jsonify, render_template

app = Flask("app")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/toggle", methods=["POST"])
def toggle():
    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")

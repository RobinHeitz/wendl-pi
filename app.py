from flask import Flask, jsonify, render_template, request

app = Flask("app")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/toggle_lamp")
def toggle():
    data = request.json
    state = data["checked"]
    print(f"It is checked: {state}")
    return jsonify({"status": "success"})

@app.route('/checkbox', methods=['POST'])
def checkbox():
    data = request.json
    checkbox_state = data['checked']
    print(f"Checkbox is {'checked' if checkbox_state else 'unchecked'}")
    return jsonify({'status': 'success'})

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")


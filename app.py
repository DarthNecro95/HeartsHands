from flask import Flask, render_template, jsonify, send_from_directory


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')


@app.route('/reports/<path:path>')
def send_report(path):
    return send_from_directory('reports', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
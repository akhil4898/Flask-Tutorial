from flask import Flask, render_template, jsonify

myApp = Flask(__name__)


@myApp.route('/')
def home():
    return render_template('index.html')


@myApp.route('/name/<string:name>/<int:age>')
def name(name, age):
    print("Hello")
    result = {
        "Age": age,
        "Name": name,
        "Server IP": "125.0.0.0",
        "Debug": True
    }
    return jsonify(result)


if __name__ == "__main__":
    myApp.run(debug=True, port=8000)
from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():
    return "<h1 style='color: red'> Hello Mobilise.</h1>"


if __name__ == '__main__':
    application.run(debug=True, port=8080)

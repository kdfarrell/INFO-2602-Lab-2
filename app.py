from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response

app.run(host='0.0.0.0', port=8080, debug=True)
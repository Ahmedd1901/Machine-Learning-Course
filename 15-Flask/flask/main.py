from flask import Flask,render_template
## create an instance of the flask class
app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to flask course"

@app.route("/index")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
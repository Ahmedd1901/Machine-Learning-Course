### jinja2 template engine
'''
{{ }} expression to print output in html
{%...%} conditions,for loops
{#...#} comments
'''
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def start():
    return "flask app"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/form" , methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'hello {name}'
    return render_template('form.html')

@app.route('/submit',methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'hello {name}'
    return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):

    return render_template('results.html',results = score)

@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 50:
        res = "passed"
    else:
        res="failed"

    exp = {'score':score, "res":res}
    return render_template('results1.html',results = exp)

if __name__ == "__main__":
    app.run(debug=True)
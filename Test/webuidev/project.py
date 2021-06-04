from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def hello():
    name = 'shakeer'
    return render_template('index.html',name2=name)

@app.route("/bootstrap")
def bootstrap():
    return  render_template('bootstrap.html')

# app.run(debug=True)
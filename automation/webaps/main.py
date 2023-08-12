from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/',methods=['POST'])
def home_post():
    print(request.form)
    dim_one = request.form["first_dim"]
    dim_two = request.form["second_dim"]
    dim_three = request.form["third_dim"]
    volume = float(dim_one) * float(dim_two) * float(dim_three)
    print("post request")
    return render_template("index.html",python_output=volume,dim_one=dim_one,dim_two=dim_two,dim_three=dim_three)

app.run(host="0.0.0.0")
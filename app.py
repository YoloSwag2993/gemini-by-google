from flask import Flask,render_template,request
import google.generativeai as palm

palm.configure(api_key="")

defaults = { 'model': "models/text-bison-001"}

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        t = request.form.get("txt")
        r = palm.generate_test(**defaults,messages=t)
        return(render_template("index.html",result=r.last))
    else:
        return(render_template("index.html",result="waiting"))

if __name__ == "__main__":
    app.run()

from flask import Flask,render_template,request
import google.generativeai as palm

palm.configure(api_key="AIzaSyD3xCtrHtzi61l9XMA4I9BiPlGXpXzp_5Q")

defaults = { 'model': "models/text-bison-001"}

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        t = request.form.get("txt")
        r = palm.generate_text(**defaults,prompt=t)
        return(render_template("index.html",result=r.result))
    else:
        return(render_template("index.html",result="waiting"))

if __name__ == "__main__":
    app.run()
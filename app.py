from flask import Flask, render_template, request
import google.generativeai as genai

genai.configure(api_key="AIzaSyD3xCtrHtzi61l9XMA4I9BiPlGXpXzp_5Q")

# Create the model object (this replaces `defaults`)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        t = request.form.get("txt")
        try:
            response = model.generate_content(t)
            return render_template("index.html", result=response.text)
        except Exception as e:
            return render_template("index.html", result=f"Error: {str(e)}")
    else:
        return render_template("index.html", result="waiting")

if __name__ == "__main__":
    app.run(debug=True)

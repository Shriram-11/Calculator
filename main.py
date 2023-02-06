from flask import Flask, render_template, request
from math import sin,tan,cos,sqrt
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        expression = request.form.get("expression")
        try:
            result = eval(expression)
        except:
            result = "Invalid expression"
        return render_template("calci.html", expression=expression, result=result)
    return render_template("calci.html")

if __name__ == "__main__":
    app.run(port=8080)

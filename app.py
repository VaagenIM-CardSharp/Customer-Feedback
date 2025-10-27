from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


file = "feedback.json"

try:
    with open(file, "r") as f:
        feedback = json.load(f)
except:
    feedback = []
    with open(file, "w") as f:
        json.dump(feedback, f)

@app.route("/")
def home():
    with open(file, "r") as f:
        data = json.load(f)
    return render_template("feedback.html", feedbacks=data)

@app.route("/submit", methods=["POST"])
def submit():
    rating = request.form["rating"]

    if not rating:
        return redirect("/")  # do nothing, just go back to home page
    
    with open(file, "r") as f:
        data = json.load(f)
    data.append({"rating": int(rating)})
    with open(file, "w") as f:
        json.dump(data, f)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
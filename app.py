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
def index():
    f = open(file, "r")
    data = json.load(f)
    f.close()
    return render_template("feedback.html", feedbacks=data)

@app.route("/submit", methods=["POST"])
def submit():
    rating = request.form.get("rating")
    comment = request.form.get("comment")

    if rating == "" or rating is None:
        return redirect("/")

    f = open(file, "r")
    data = json.load(f)
    f.close()

    data.append({
        "rating": int(rating),
        "comment": comment
    })

    f = open(file, "w")
    json.dump(data, f)
    f.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

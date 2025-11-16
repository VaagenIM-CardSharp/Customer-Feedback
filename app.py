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

# Opens Json file and creates a new listing
@app.route("/")
def index():
    f = open(file, "r")
    data = json.load(f)
    f.close()
    return render_template("feedback.html", feedbacks=data)

# Recives feedback data from the form and reads it
@app.route("/submit", methods=["POST"])
def submit():
    rating = request.form.get("rating")
    comment = request.form.get("comment")

# Redirects user back to the main page if no rating is given
    if rating == "" or rating is None:
        return redirect("/")

# Adds the feedback data into the Json file and sorts it into a rating and comment category
    f = open(file, "r")
    data = json.load(f)
    f.close()

    data.append({
        "rating": int(rating),
        "comment": comment
    })

# Saves the new listing in the Json file and reidrects the user back to the main page
    f = open(file, "w")
    json.dump(data, f)
    f.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

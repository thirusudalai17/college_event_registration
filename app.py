from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)
DATA_FILE = "registrations.csv"

EVENTS = [
    {"id": "coding", "name": "Coding Contest", "date": "2026-10-05", "time": "10:00 AM"},
    {"id": "web", "name": "Web Design Workshop", "date": "2026-10-10", "time": "2:00 PM"},
    {"id": "cultural", "name": "Cultural Fest", "date": "2026-10-15", "time": "5:00 PM"}
]

def save_registration(data):
    file_exists = os.path.exists(DATA_FILE)
    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "name", "register_no", "department", "year", "event", "email"
        ])
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

@app.route("/")
def home():
    return render_template("index.html", events=EVENTS)

@app.route("/register", methods=["POST"])
def register():
    data = {
        "name": request.form["name"].strip(),
        "register_no": request.form["register_no"].strip(),
        "department": request.form["department"],
        "year": request.form["year"],
        "event": request.form["event"],
        "email": request.form["email"].strip()
    }
    save_registration(data)
    return redirect(url_for("success", name=data["name"], event=data["event"]))

@app.route("/success")
def success():
    return render_template(
        "success.html",
        name=request.args.get("name", "Student"),
        event=request.args.get("event", "")
    )

@app.route("/admin")
def admin():
    registrations = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, newline="", encoding="utf-8") as file:
            registrations = list(csv.DictReader(file))
    return render_template("admin.html", registrations=registrations)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, session
import pandas as pd
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secure_key_2026"

# Load dataset
data = pd.read_csv("stroke_prediction_dataset.csv")

# Database connection
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# ---------------- HOME / LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()

        if user and check_password_hash(user["password"], password):
            session["user"] = username
            return redirect("/dashboard")

    return render_template("login.html")


# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if len(username) < 3 or len(password) < 5:
            return "Username must be at least 3 characters and password at least 5 characters"

        password = generate_password_hash(password)

        db = get_db()
        db.execute("INSERT INTO users(username, password) VALUES (?,?)", (username, password))
        db.commit()

        return redirect("/")

    return render_template("register.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")
    return render_template("dashboard.html")


# ---------------- DATASET PAGE ----------------
@app.route("/dataset")
def dataset():
    table = data.head(20).to_html()
    return render_template("dataset.html", table=table)


# ---------------- ADD PATIENT ----------------
@app.route("/add", methods=["GET", "POST"])
def add_patient():

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        glucose = request.form["glucose"]
        bmi = request.form["bmi"]

        db = get_db()
        db.execute("INSERT INTO patients(name, age, glucose, bmi) VALUES (?,?,?,?)",
                   (name, age, glucose, bmi))
        db.commit()

        return redirect("/patients")

    return render_template("add_patient.html")


# ---------------- VIEW PATIENTS ----------------
@app.route("/patients")
def patients():

    db = get_db()
    patients = db.execute("SELECT * FROM patients").fetchall()

    return render_template("patients.html", patients=patients)


# ---------------- DELETE PATIENT ----------------
@app.route("/delete/<int:id>")
def delete_patient(id):

    db = get_db()
    db.execute("DELETE FROM patients WHERE id=?", (id,))
    db.commit()

    return redirect("/patients")


# ---------------- EDIT PATIENT ----------------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_patient(id):

    db = get_db()

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        glucose = request.form["glucose"]
        bmi = request.form["bmi"]

        db.execute("UPDATE patients SET name=?, age=?, glucose=?, bmi=? WHERE id=?",
                   (name, age, glucose, bmi, id))
        db.commit()

        return redirect("/patients")

    patient = db.execute("SELECT * FROM patients WHERE id=?", (id,)).fetchone()

    return render_template("edit_patient.html", patient=patient)


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)
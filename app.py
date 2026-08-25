from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "Database")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = "change_this_secret_key"


def json_path(filename):
    return os.path.join(DATA_DIR, filename)


# ---------------- CREATE JSON FILES ----------------

os.makedirs(DATA_DIR, exist_ok=True)

files = [
    "students.json",
    "assessments.json",
    "questions.json",
    "results.json",
]

for file in files:
    path = json_path(file)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump([], f)

# Populate default users when the students file is empty.
students_path = json_path("students.json")
with open(students_path, "r", encoding="utf-8") as f:
    try:
        existing_students = json.load(f)
    except json.JSONDecodeError:
        existing_students = []

if not existing_students:
    default_students = [
        {"username": "admin", "password": "admin123", "role": "admin"},
        {"username": "student", "password": "student123", "role": "student"},
    ]
    with open(students_path, "w", encoding="utf-8") as f:
        json.dump(default_students, f, indent=4)


# ---------------- FUNCTIONS ----------------

def load_students():
    with open(json_path("students.json"), "r", encoding="utf-8") as f:
        return json.load(f)


def save_students(data):
    with open(json_path("students.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_assessments():
    with open(json_path("assessments.json"), "r", encoding="utf-8") as f:
        return json.load(f)


def save_assessments(data):
    with open(json_path("assessments.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_questions():
    with open(json_path("questions.json"), "r", encoding="utf-8") as f:
        return json.load(f)


def save_questions(data):
    with open(json_path("questions.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_results():
    with open(json_path("results.json"), "r", encoding="utf-8") as f:
        return json.load(f)


def save_results(data):
    with open(json_path("results.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("login.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        role = request.form.get("role", "student").strip().lower()

        students = load_students()
        for s in students:
            if s.get("username") == username and s.get("password") == password and s.get("role") == role:
                session["username"] = username
                session["role"] = role
                if role == "admin":
                    return redirect(url_for("admin_dashboard"))
                return redirect(url_for("student_dashboard"))

        # Auto-register any new user credentials in students.json
        students.append({"username": username, "password": password, "role": role})
        save_students(students)
        session["username"] = username
        session["role"] = role
        if role == "admin":
            return redirect(url_for("admin_dashboard"))
        return redirect(url_for("student_dashboard"))

    return render_template("login.html")


def get_assessments():
    return load_assessments()


def get_assessment_by_id(assessment_id):
    for assessment in get_assessments():
        if assessment.get("assessment_id") == assessment_id:
            return assessment
    return None


def get_questions_for_assessment(assessment_id):
    return [q for q in load_questions() if q.get("assessment_id") == assessment_id]


def get_student_results(username):
    return [result for result in load_results() if result.get("student_name") == username]


# ---------------- ADMIN DASHBOARD ----------------

@app.route("/admin_dashboard")
def admin_dashboard():
    if session.get("role") != "admin":
        return redirect(url_for("home"))
    return render_template("admin_dashboard.html", assessments=get_assessments())


# ---------------- STUDENT DASHBOARD ----------------

@app.route("/student_dashboard")
def student_dashboard():
    if session.get("role") != "student":
        return redirect(url_for("home"))
    return render_template("student_dashboard.html", assessments=get_assessments())


# ---------------- CREATE ASSESSMENT ----------------

@app.route("/create_assessment", methods=["GET", "POST"])
def create_assessment():
    if session.get("role") != "admin":
        return redirect(url_for("home"))

    if request.method == "POST":
        assessments = get_assessments()
        next_id = len(assessments) + 1
        assessments.append({
            "assessment_name": request.form["assessment_name"],
            "subject": request.form["subject"],
            "assessment_id": next_id,
        })
        save_assessments(assessments)
        return redirect(url_for("admin_dashboard"))

    return render_template("create_assessment.html")


# ---------------- VIEW ASSESSMENT ----------------

@app.route("/view_assessment")
def view_assessment():
    assessments = get_assessments()
    return render_template("view_assessment.html", assessments=assessments)


# ---------------- ADD QUESTIONS ----------------

@app.route("/add_questions", methods=["GET", "POST"])
def add_questions():
    if session.get("role") != "admin":
        return redirect(url_for("home"))

    assessments = get_assessments()
    if request.method == "POST":
        questions = load_questions()
        assessment_id = int(request.form["assessment_id"])
        assessment = get_assessment_by_id(assessment_id)
        questions.append({
            "assessment_id": assessment_id,
            "assessment_name": assessment.get("assessment_name") if assessment else "",
            "question": request.form["question"],
            "option_a": request.form["option_a"],
            "option_b": request.form["option_b"],
            "option_c": request.form["option_c"],
            "option_d": request.form["option_d"],
            "correct_answer": request.form["correct_answer"],
        })
        save_questions(questions)
        return redirect(url_for("admin_dashboard"))

    return render_template("add_questions.html", assessments=assessments)


# ---------------- ASSESSMENT ----------------

@app.route("/assessment")
def assessment():
    if session.get("role") != "student":
        return redirect(url_for("home"))

    assessment_id = request.args.get("assessment_id", type=int)
    assessments = get_assessments()
    if not assessments:
        return render_template("student_dashboard.html", assessments=assessments)

    if assessment_id is None:
        assessment_id = assessments[0].get("assessment_id")

    assessment = get_assessment_by_id(assessment_id)
    questions = get_questions_for_assessment(assessment_id)

    return render_template(
        "assessment.html",
        assessment_name=assessment.get("assessment_name") if assessment else "Assessment",
        questions=questions,
        assessment_id=assessment_id,
    )


# ---------------- SUBMIT ASSESSMENT ----------------
@app.route("/submit_assessment", methods=["POST"])
def submit_assessment():
    if session.get("role") != "student":
        return redirect(url_for("home"))

    assessment_id = int(request.form.get("assessment_id", 0))
    questions = get_questions_for_assessment(assessment_id)
    total_questions = len(questions)
    correct_count = 0
    for index, question in enumerate(questions, start=1):
        answer = request.form.get(f"q{index}")
        if answer == question.get("correct_answer"):
            correct_count += 1

    percentage = int((correct_count / total_questions) * 100) if total_questions else 0
    result_text = "Pass" if percentage >= 50 else "Fail"
    student_name = session.get("username", "Student")
    assessment = get_assessment_by_id(assessment_id) or {}

    results = load_results()
    results.append({
        "student_name": student_name,
        "assessment_name": assessment.get("assessment_name", "Assessment"),
        "assessment_id": assessment_id,
        "total_questions": total_questions,
        "correct_answers": correct_count,
        "marks": correct_count,
        "percentage": percentage,
        "result": result_text,
    })
    save_results(results)

    return render_template(
        "result.html",
        student_name=student_name,
        assessment_name=assessment.get("assessment_name", "Assessment"),
        total_questions=total_questions,
        correct_answers=correct_count,
        marks=correct_count,
        percentage=percentage,
        result=result_text,
        back_url=url_for("student_dashboard"),
    )


# ---------------- RESULT ----------------
@app.route("/result")
def result():
    if session.get("role") != "student":
        return redirect(url_for("home"))

    student_name = session.get("username")
    student_results = get_student_results(student_name)
    latest = student_results[-1] if student_results else None
    if latest:
        return render_template(
            "result.html",
            student_name=latest.get("student_name"),
            assessment_name=latest.get("assessment_name"),
            total_questions=latest.get("total_questions"),
            correct_answers=latest.get("correct_answers"),
            marks=latest.get("marks"),
            percentage=latest.get("percentage"),
            result=latest.get("result"),
            back_url=url_for("student_dashboard"),
        )

    return render_template(
        "result.html",
        student_name="Student",
        assessment_name="No Assessment",
        total_questions=0,
        correct_answers=0,
        marks=0,
        percentage=0,
        result="No result yet",
        back_url=url_for("student_dashboard"),
    )


# ---------------- VIEW RESULTS ----------------
@app.route("/view_results")
def view_results():
    if session.get("role") != "admin":
        return redirect(url_for("home"))
    return render_template("admin_result.html", results=load_results())


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


# ---------------- ADMIN RESULT ----------------

@app.route("/admin_result")
def admin_result():

    results = load_results()

    return render_template(
        "admin_result.html",
        results=results
    )


# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)
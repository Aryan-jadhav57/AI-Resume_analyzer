from flask import Flask, render_template, request, redirect, session
from ai import analyze_resume
from db import engine, Base, SessionLocal
from models import User, Reports   # import your models
import PyPDF2
import docx
import json

app = Flask(__name__)
app.secret_key = 'secret123'

# ✅ Create tables before starting the app
Base.metadata.create_all(bind=engine)

# HOME Page
@app.route('/')
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")


# SIGNUP page
@app.route("/signup", methods=["GET", "POST"])
def signup():
    db = SessionLocal()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # ✅ Correct usage of User model
        existing_user = db.query(User).filter_by(email=email).first()
        if existing_user:
            db.close()
            return "User already Exists"
        
        user = User(email=email, password=password)

        db.add(user)
        db.commit()
        db.close()  # always close session

        return redirect("/login")
    
    # ✅ remove leading slash in template name
    return render_template("signup.html")


# LOGIN 
@app.route("/login", methods=["GET", "POST"])
def login():
    db = SessionLocal()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = db.query(User).filter_by(email=email, password=password).first()

        if user:
            session["user"] = user.email
            db.close()
            return redirect("/dashboard")
        else:
            db.close()
            return "Invalid credentials"
        
    return render_template("login.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect('/login')
    
    result = None
    resume_text = None
    user_goal = None

    if request.method == "POST":
        user_goal = request.form.get("role")
        resume_text = request.form.get("resume")
        file = request.files.get("file")

        # File handling
        if file and file.filename != "":
            if file.filename.endswith(".pdf"):
                try:
                    pdf_reader = PyPDF2.PdfReader(file)
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text() or ""
                    resume_text = text
                except Exception as e:
                    result = {"error": f"PDF error: {str(e)}"}

            elif file.filename.endswith(".docx"):
                try:
                    doc = docx.Document(file)
                    text = ""
                    for para in doc.paragraphs:
                        text += para.text + "\n"
                    resume_text = text
                except Exception as e:
                    result = {"error": f"Docx error: {str(e)}"}

    # ✅ Safe check — resume_text always exists now
    if resume_text and user_goal:
        try:
            result = analyze_resume(resume_text, user_goal)

            db = SessionLocal()
            user = db.query(User).filter_by(email=session["user"]).first()

            report = Reports(
                user_id=user.id,
                resume_text=resume_text,
                result=json.dumps(result)
            )

            db.add(report)
            db.commit()
            db.close()

        except Exception as e:
            result = {"error": f"AI error: {str(e)}"}

    return render_template(
        "dashboard.html",
        user=session["user"],
        result=result
    )


# history
@app.route("/history")
def history():
    if "user" not in session:
        return redirect('/login')
    
    db = SessionLocal()
    user = db.query(User).filter_by(email=session["user"]).first()
    reports = db.query(Reports).filter_by(user_id = user.id).all()

    #convert JSON string > dict
    pasred_reports = []
    for r in reports:
        try:
            pasred_result = json.loads(r.result)
        except:
            pasred_result = []

        pasred_reports.append({
            "resume": r.resume_text,
            'result':pasred_result

        })

    return render_template("history.html", reports=pasred_reports)
            
#logout
@app.route("/logout")
def logout():
    session.pop("user", None )
    return redirect('/login')
    


if __name__ == "__main__":
    app.run(debug=True)

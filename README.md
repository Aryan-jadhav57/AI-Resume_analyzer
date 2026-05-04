
# AI Resume Analyzer

AI Resume Analyzer is a Flask-based web application that helps users evaluate their resumes using AI.  
It provides actionable insights such as **skills analysis, missing skills, career roadmap, and interview questions** based on the user’s target role.

---

## 🚀 Features
- 🔐 **User Authentication** (Signup/Login with session management)
- 📂 **Resume Upload** (Supports `.pdf` and `.docx`)
- 📝 **Text Input** (Paste resume directly into the form)
- 🤖 **AI-Powered Analysis** (Integrates with OpenAI API for resume evaluation)
- 💾 **Database Storage** (SQLAlchemy ORM with persistent user reports)
- 📊 **Dashboard** (View latest resume analysis results)
- 📜 **History Page** (Access past resume analyses)
- 🔒 **Logout** (Secure session termination)

---

## 🛠️ Tech Stack
- **Backend**: Flask, SQLAlchemy
- **Frontend**: Jinja2 Templates, HTML/CSS
- **Database**: MySQL / PostgreSQL (via SQLAlchemy ORM)
- **AI Integration**: OpenAI API
- **File Parsing**: PyPDF2, python-docx
- **Session Management**: Flask sessions

---

## 📂 Project Structure
```
AI-Resume-Analyzer/
│── ai.py              # AI integration logic (OpenAI API calls)
│── app.py             # Main Flask application
│── db.py              # Database engine and session setup
│── models.py          # SQLAlchemy models (User, Reports)
│── templates/         # Jinja2 HTML templates (signup, login, dashboard, history)
│── static/            # CSS/JS assets
│── requirements.txt   # Dependencies
│── README.md          # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-resume-analyzer.git
   cd ai-resume-analyzer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Create a `.env` file in the project root:
     ```
     OPENAI_API_KEY=your_api_key_here
     DATABASE_URL=mysql+pymysql://user:password@localhost/resume_db
     ```

5. **Run the application**
   ```bash
   python app.py
   ```
   Visit `http://127.0.0.1:5000` in your browser.

---

## 📸 Screenshots
- **Signup/Login Page**
- **Dashboard with Resume Analysis**
- **History of Reports**

---

## 🔮 Future Enhancements
- Add **role-specific recommendations** (e.g., Backend Developer, Data Scientist)
- Export analysis results as **PDF/Excel**
- Integrate **ATS score prediction**
- Add **multi-language support**

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License
This project is licensed under the MIT License.
```

import os, re
from io import BytesIO
from flask import Flask, render_template, request, session, send_file
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from agents import *
from report_generator import build_report

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY","dev")

limiter = Limiter(get_remote_address, app=app, storage_uri="memory://")

def extract_score(text):
    match = re.search(r'(\b\d{2,3}\b)', text)
    if match:
        return min(int(match.group(1)),100)
    return 60



def strip_emojis(text: str) -> str:
    # Remove most emoji / pictographs to ensure plain professional output
    emoji_ranges = (
        (0x1F300, 0x1F5FF),
        (0x1F600, 0x1F64F),
        (0x1F680, 0x1F6FF),
        (0x1F700, 0x1F77F),
        (0x1F780, 0x1F7FF),
        (0x1F800, 0x1F8FF),
        (0x1F900, 0x1F9FF),
        (0x1FA00, 0x1FAFF),
        (0x2700, 0x27BF),
        (0x2600, 0x26FF),
    )

    def is_emoji(ch: str) -> bool:
        cp = ord(ch)
        for a, b in emoji_ranges:
            if a <= cp <= b:
                return True
        return False

    return "".join(ch for ch in (text or "") if not is_emoji(ch))


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
@limiter.limit("3/hour")
def run():
    cv = request.form["cv"]
    job = request.form["job"]
    role = request.form.get("role")
    lang = request.form.get("lang","en")
    culture = request.form.get("culture")
    reviews = request.form.get("reviews")
    company = request.form.get("company")

    match = recruiter_match(cv, job, role, lang)
    optimized = optimize_cv(cv, match, lang)
    # Store enhanced CV (plain text, no emoticons)
    session["enhanced_cv_txt"] = strip_emojis(optimized)
    ats = ats_audit(optimized, lang)
    ats_cv = ats_submission(optimized, lang)
    interview = interview_pack(optimized, job, role, lang)
    deep = requirement_intelligence(cv, job, role, lang)
    hire = hireability_score(cv, job, role, lang)
    psyche = recruiter_psychology(cv, job, role, lang)

    culture_report = None
    if culture and reviews:
        culture_report = culture_analysis(culture, reviews, company, lang)

    hire_score = extract_score(hire)
    match_score = extract_score(match)

    session["report"] = {
        "Requirement Intelligence": deep,
        "Hireability Impression": hire,
        "Recruiter Psychology": psyche,
        "Recruiter Match": match,
        "Optimized CV": optimized,
        "ATS Audit": ats,
        "ATS Submission CV": ats_cv,
        "Interview Pack": interview,
        "Culture Analysis": culture_report or ""
    }

    return render_template("dashboard.html",
        hire_score=hire_score,
        match_score=match_score,
        deep=deep, hire=hire, psyche=psyche,
        match=match, optimized=optimized,
        ats=ats, ats_cv=ats_cv,
        interview=interview,
        culture=culture_report
    )

@app.route("/download")
def download():
    data = session.get("report")
    if not data:
        return "No report", 400
    file = build_report(data)
    return send_file(file,
        as_attachment=True,
        download_name="AI_Job_Hunt_v5_Report.docx",
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )


@app.route("/download_cv")
def download_cv():
    enhanced = session.get("enhanced_cv_txt")
    if not enhanced:
        return "No enhanced CV available. Run an analysis first.", 400

    return send_file(
        BytesIO(enhanced.encode("utf-8")),
        as_attachment=True,
        download_name="enhanced_cv.txt",
        mimetype="text/plain; charset=utf-8"
    )


@app.route("/health")
def health():
    return {"status":"ok"}

from openai_client import llm

def lang_rule(lang):
    return "Respond in Swedish." if lang == "sv" else "Respond in English."

# ---- Module 1 ----
def recruiter_match(cv, job, role, lang):
    return llm(f"You are a senior recruiter. {lang_rule(lang)}",
               f"Provide numeric match score (0-100), gaps and blockers. CV:{cv} JOB:{job} ROLE:{role}")

# ---- Module 2 ----
def optimize_cv(cv, match, lang):
    return llm(f"You are a CV strategist using X-Y-Z. {lang_rule(lang)}",
               f"Rewrite CV experience based on: {match} CV:{cv}")

# ---- Module 3 ----
def ats_audit(cv, lang):
    return llm(f"You are an ATS system. {lang_rule(lang)}",
               f"Provide ATS risks and fixes. CV:{cv}")

# ---- Module 4 ----
def ats_submission(cv, lang):
    return llm(f"You generate ATS-optimized CV. {lang_rule(lang)}",
               f"Rewrite CV in one-column ATS format. CV:{cv}")

# ---- Modules 5,7,8 ----
def interview_pack(cv, job, role, lang):
    return llm(f"You are a hiring manager and HR partner. {lang_rule(lang)}",
               f"Generate technical, HR, and candidate questions. CV:{cv} JOB:{job} ROLE:{role}")

# ---- Module 6 ----
def culture_analysis(culture, reviews, company, lang):
    return llm(f"You analyze company culture vs reviews. {lang_rule(lang)}",
               f"Compare official culture and employee reviews. COMPANY:{company} CULTURE:{culture} REVIEWS:{reviews}")

# ---- Enhancement 1 ----
def requirement_intelligence(cv, job, role, lang):
    return llm(f"You deeply analyze job requirements. {lang_rule(lang)}",
               f"Break job into core skills, hidden signals, seniority expectations, impact, deal-breakers, and alignment strength. CV:{cv} JOB:{job} ROLE:{role}")

# ---- Enhancement 2 ----
def hireability_score(cv, job, role, lang):
    return llm(f"You calculate weighted hireability score. {lang_rule(lang)}",
               f"Return numeric hireability score (0-100) and explanation. CV:{cv} JOB:{job} ROLE:{role}")

# ---- Enhancement 3 ----
def recruiter_psychology(cv, job, role, lang):
    return llm(f"You simulate recruiter psychology. {lang_rule(lang)}",
               f"Simulate 30-second recruiter scan reaction, doubts, curiosity, seniority perception. CV:{cv} JOB:{job} ROLE:{role}")

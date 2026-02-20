# CareerSverigeAI

# AI Job Hunt v5 -- Complete Intelligence Platform

AI Job Hunt v5 is a full-stack AI Career Intelligence Platform that
analyzes a candidate's CV against a job description using recruiter
simulation, strategic modeling, and psychological insights.

This is not just a CV optimizer --- it is a structured, multi-module
career intelligence engine.

------------------------------------------------------------------------

## Core Modules (1--8)

1.  Recruiter Match Analysis\
2.  CV Optimization (X--Y--Z impact rewrite)\
3.  ATS Audit\
4.  ATS Submission CV\
5.  Technical Interview Preparation\
6.  Company Culture: Reality vs Image\
7.  HR / Behavioral Interview Questions\
8.  Candidate Strategic Questions

------------------------------------------------------------------------

## Advanced Enhancements

### Requirement Intelligence Engine

-   Core skills extraction
-   Hidden job signals
-   Seniority expectations
-   Business impact analysis
-   Deal-breaker detection
-   Alignment strength scoring

### Hireability Impression Score

Weighted recruiter-style scoring (0--100): - Skill alignment - Seniority
fit - Business impact clarity - ATS readiness - Positioning strength

### Recruiter Psychology Simulation

-   30-second scan reaction
-   Doubt triggers
-   Curiosity hooks
-   Seniority perception
-   Emotional hiring inclination

------------------------------------------------------------------------

## Executive Dashboard

-   Visual Hireability Score Bar
-   Visual Recruiter Match Score Bar
-   Matrix-style interface
-   Structured intelligence breakdown

------------------------------------------------------------------------

## Download Options

After analysis:

-   `/download` â Full intelligence report (DOCX)
-   `/download_cv` â Enhanced CV as plain text (.txt, no emoticons)

------------------------------------------------------------------------

## Production Features

-   Matrix UI theme
-   English / Swedish language support
-   Rate limiting (3/hour per IP)
-   No database dependency
-   Railway-ready deployment
-   Health endpoint: `/health`

------------------------------------------------------------------------

## Installation (Local)

``` bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`:

    OPENAI_API_KEY=your_key_here
    OPENAI_MODEL=gpt-4.1-mini
    SECRET_KEY=change_me

Run:

``` bash
flask --app app run
```

------------------------------------------------------------------------

## Railway Deployment

1.  Push to GitHub
2.  Connect Railway
3.  Add environment variables:
    -   OPENAI_API_KEY
    -   SECRET_KEY
4.  Deploy

Health check: `/health`

------------------------------------------------------------------------

## Architecture Flow

User Input â\
Recruiter Match â\
CV Optimization â\
ATS Audit â\
ATS Submission â\
Interview Pack â\
Requirement Intelligence â\
Hireability Score â\
Recruiter Psychology â\
Executive Dashboard + Downloads

------------------------------------------------------------------------

## Positioning

AI Career Intelligence Platform\
Recruiter Simulation Engine\
Strategic Hiring Optimization System

Suitable for professionals, career coaches, universities, and SaaS
commercialization.

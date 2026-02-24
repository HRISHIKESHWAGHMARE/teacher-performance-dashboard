# Teacher Performance Dashboard

This project is a dashboard replication and enhancement task completed as part of a Data Analyst hiring assignment.  
The original dashboard was built in R Shiny and has been recreated using Python.

---

## Objective
- Replicate the structure of the original dashboard
- Improve UI/UX and readability
- Implement clean data modeling and metrics
- Provide meaningful interactivity and insights

---

## Tech Stack
- Python
- Streamlit (UI layer only)
- Pandas
- Plotly

---

## Dashboard Sections
- **Dashboard** – Overall KPIs and performance trends
- **Teacher** – Individual teacher performance analysis
- **Late Count & Attrition** – Attendance and attrition insights

---

## Key Features
- Modular code structure
- Centralized data loading and metrics
- Role-ready authentication design
- Interactive charts and filters
- Clean, professional UI

---

## Assumptions
- One teacher can have multiple evaluations
- Overall score is the average of skill-level scores
- Late count is aggregated monthly
- Attrition score above 3.5 indicates high risk

---

## How to Run the Project
```bash
pip install -r requirements.txt
streamlit run app.py
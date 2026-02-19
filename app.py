import streamlit as st
from planner import create_plan
from resume_analyzer import analyze_resume

st.set_page_config(page_title="Agentic AI Career Assistant", layout="wide")

st.title("🚀 Agentic AI Career Assistant")
st.write("Guide Planner + Resume Mentor using Gemini AI")

tab1, tab2 = st.tabs(["📍 Guide Planner", "📄 Resume Mentor"])

# --- Guide Planner ---
with tab1:
    st.subheader("Enter your career goal")

    goal = st.text_input("Example: Become a Machine Learning Engineer")

    if st.button("Generate Roadmap"):
        if goal.strip() == "":
            st.warning("Please enter a goal")
        else:
            with st.spinner("Planning your roadmap..."):
                result = create_plan(goal)
                st.write(result)

# --- Resume Mentor ---
with tab2:
    st.subheader("Paste your resume text")

    resume = st.text_area("Paste resume here", height=250)

    if st.button("Analyze Resume"):
        if resume.strip() == "":
            st.warning("Please paste your resume")
        else:
            with st.spinner("Analyzing resume..."):
                result = analyze_resume(resume)
                st.write(result)

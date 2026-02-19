from agents import get_llm

def analyze_resume(resume_text):
    model = get_llm()

    prompt = f"""
    You are a professional Resume Mentor.

    Review the resume below and give:

    1. Strengths
    2. Weaknesses
    3. Missing skills
    4. Improved bullet points
    5. Final rating out of 10

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)
    return response.text

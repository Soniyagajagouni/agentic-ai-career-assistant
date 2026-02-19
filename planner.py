from agents import get_llm

def create_plan(goal):
    model = get_llm()

    prompt = f"""
    You are an AI Career Guide Planner.

    Create a structured roadmap for this goal:
    {goal}

    Include:
    - Skills to learn
    - Projects to build
    - Timeline
    - Tools to use
    - Final career outcome
    """

    response = model.generate_content(prompt)
    return response.text

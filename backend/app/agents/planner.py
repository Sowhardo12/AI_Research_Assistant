from app.core.llm import client

def planner_agent(topic: str) -> list[str]:
    prompt = f"""
You are a research planner.
Break the topic into EXACTLY 3 research questions.
Keep each question under 15 words.

Return the output as a numbered list ONLY.

Topic: {topic}

Return ONLY a numbered list.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=300,
    )

    content = response.choices[0].message.content
    questions = [line.strip("12345. ") for line in content.split("\n") if line.strip()]
    return questions

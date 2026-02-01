from app.core.llm import client

def research_agent(question: str) -> str:
    prompt = f"""
Answer the question concisely.
Use bullet points.
Maximum 5 bullets.
Each bullet under 20 words.
Question: {question}
[keep response short and concise for less token usage]
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=500,
    )

    return response.choices[0].message.content

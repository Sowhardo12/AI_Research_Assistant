from app.core.llm import client

def critic_agent(text: str) -> str:
    prompt = f"""
You are a reviewer.

Identify:
- Missing perspectives (if any)
- Weak or vague points

Respond in max 5 bullet points.
Be concise.

Text:
{text}
[keep response short and concise for less token usage]
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=300,
    )

    return response.choices[0].message.content

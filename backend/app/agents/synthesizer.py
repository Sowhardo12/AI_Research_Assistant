from app.core.llm import client

def synthesizer_agent(research: list[str], critique: str) -> str:
    prompt = f"""
Produce a final structured research summary.

Rules:
- Clear sections
- Bullet points
- Address critique briefly
- No fluff
Research:
{research}
Critique:
{critique}

[keep response short and concise for less token usage]
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=800,
    )

    return response.choices[0].message.content

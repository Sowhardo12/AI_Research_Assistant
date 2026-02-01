from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.planner import planner_agent
from app.agents.researcher import research_agent
from app.agents.critic import critic_agent
from app.agents.synthesizer import synthesizer_agent

router = APIRouter()

class ResearchRequest(BaseModel):
    topic: str #type string
@router.post("/research")
async def research_topic(request: ResearchRequest):
    questions = planner_agent(request.topic)
    research_results = []
    for question in questions:
        research_results.append(research_agent(question)) 
    critique = critic_agent(" ".join(research_results))
    #compiling all results 
    final_answer = synthesizer_agent(research_results,critique)   
    return {
        "topic": request.topic,
        "questions": questions,
        "final_answer": final_answer
    }
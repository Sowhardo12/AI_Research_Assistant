from fastapi import FastAPI
from app.routes.research import router as research_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Research Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(research_router)


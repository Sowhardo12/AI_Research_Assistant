# Multi-Agent Research Assistant

An asynchronous, modular agent orchestration system designed to automate deep research workflows. The application utilizes a FastAPI backend to coordinate multiple specialized LLM agents via the Groq API, aggregates their findings, and serves structured insights to a clean React frontend.

## Features
* **Multi-Agent Orchestration:** Implements task delegation logic to split a research query among specialized sub-agents.
* **Asynchronous Execution:** Built with FastAPI to handle concurrent API calls and response generation efficiently.
* **Response Aggregation:** Automatically synthesizes data from multiple agents into a single, cohesive, and structured markdown report.
* **Lightweight UI:** A minimal React dashboard to submit research topics and view real-time outputs.

## Tech Stack
* **Backend:** Python, FastAPI, Groq API (LLM Orchestration)
* **Frontend:** React.js, Tailwind CSS
* **Environment & Tools:** Asynchronous Programming (`asyncio`), HTTPX


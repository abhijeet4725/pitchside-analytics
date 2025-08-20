Pitchside Analytics
Pitchside Analytics is an intelligent AI agent designed for AgentHack 2025. This project provides a natural language interface for real-time football analytics, offering deep insights into season standings, match statistics, and player performance. Powered by FastAPI, Portia AI, and the Gemini Pro LLM, the agent seamlessly interacts with the API-Football data source to deliver professional-grade analysis in a conversational format.

Key Features
Natural Language Queries: Users can interact with the agent using conversational English, making complex data retrieval as simple as asking a question.

Season Analytics: Get high-level insights on league standings, top scorers, and team performance across an entire season.

Match Analytics: Access detailed, game-specific data, including goal scorers, events, and key statistics from individual matches.

Technology Stack
The project is built on a modern agentic stack to ensure performance, scalability, and security.

FastAPI: Serves as the high-performance backend, providing a robust and well-documented API.

Portia AI: The core agentic framework that orchestrates the entire system. It intelligently plans and executes multi-step tasks by utilizing available tools.

Gemini Pro: The large language model (LLM) that powers the agent's reasoning, turning natural language queries into executable plans and raw data into polished responses.

API-Football: The definitive data source for all football information, providing the raw statistical data that powers the agent's analysis.

Python-Dotenv: A library to securely manage API keys and other sensitive configuration.

Project Structure
The codebase is organized in a modular and maintainable structure:

/pitchside-analytics/
├── .env
├── main.py
└── /app
    ├── __init__.py
    ├── /tools
    │   ├── __init__.py
    │   └── football_tools.py
    └── /api
        ├── __init__.py
        └── endpoints.py

Getting Started
1. Clone the Repository
Clone the project to your local machine and navigate into the directory.

git clone https://github.com/your-username/pitchside-analytics.git
cd pitchside-analytics

2. Set Up the Environment
Create and activate a Python virtual environment.

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
Install all required libraries using pip.

pip install fastapi "uvicorn[standard]" python-dotenv portia-sdk-python requests

4. Configure API Keys
Create a .env file in the project's root directory and add your API keys. Do not commit this file to Git.

# .env file
GOOGLE_API_KEY=your_gemini_api_key_here
API_FOOTBALL_KEY=your_api_football_key_here

5. Run the Application
Start the FastAPI server.

uvicorn main:app --reload

How to Use
Once the server is running, you can interact with the agent's API at http://127.0.0.1:8000/docs. From there, you can use the interactive interface to test your queries.

Example Queries:

"Show me the current standings for the Premier League 2024 season."

"Who were the top 10 goal scorers in La Liga in 2023?"

"What were the key events in the last match between Arsenal and Manchester United?"

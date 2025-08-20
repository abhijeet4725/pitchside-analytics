import os  # The 'os' library is used to interact with the operating system, specifically to get environment variables.
import requests  # The 'requests' library is a powerful HTTP client for Python, used to make API calls.
from pydantic import BaseModel, Field  # 'pydantic' is used by Portia AI to define data models and validate data.
from typing import List, Dict, Any  # 'typing' is used for type hints, which makes code more readable.
from portia import Function  # 'Function' is a decorator from Portia AI that marks a function as a callable tool for the agent.

# --- API Configuration ---

# This gets your secret API key from the .env file. It's crucial for security.
# 'os.getenv' is the standard way to retrieve environment variables.
API_FOOTBALL_KEY = os.getenv("API_FOOTBALL_KEY")
# This is the base URL for the API-Football service. All requests will start with this.
BASE_URL = "https://v3.football.api-sports.io"

# --- Helper Data for the Agent ---

# This dictionary maps the common name of a league (what a user would say)
# to the unique ID that the API-Football service understands.
LEAGUE_MAP = {
    "premier league": 39,
    "la liga": 140,
    "bundesliga": 78,
    "serie a": 135,
    "ligue 1": 61,
    "mls": 253,
    "champions league": 2,
}

# This is a helper function to quickly get the ID.
def _get_league_id(league_name: str) -> int:
    """Helper function to get the league ID from its name."""
    # '.get()' is a safe way to access a dictionary. If the name isn't found, it returns None.
    return LEAGUE_MAP.get(league_name.lower())

# --- Custom Tools for the Portia AI Agent ---

# The '@Function' decorator tells Portia AI that this function is a tool it can use.
# The docstring below is the most important part!
# The AI agent reads this to understand what the tool does and what arguments it needs.
@Function
def get_league_standings(league_name: str, season: str) -> List[Dict[str, Any]]:
    """
    Retrieves the current standings for a specified football league and season.
    This is useful for getting the rank, team name, points, and other stats for all teams in a league.

    Args:
        league_name: The name of the football league (e.g., "Premier League").
        season: The year of the season (e.g., "2024").

    Returns:
        A list of dictionaries, where each dictionary represents a team's standing.
    """
    # Use the helper function to get the ID.
    league_id = _get_league_id(league_name)
    # If the ID isn't found, return a formatted error message.
    if not league_id:
        return {"error": f"Could not find a league with the name '{league_name}'."}

    # This dictionary holds the required headers for the API request.
    # The 'x-rapidapi-key' is your API key for authentication.
    headers = {
        'x-rapidapi-key': API_FOOTBALL_KEY,
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }

    # This dictionary holds the query parameters for the API.
    params = {
        'league': league_id,
        'season': season
    }

    # The full URL for the API endpoint.
    endpoint = f"{BASE_URL}/standings"

    try:
        # 'requests.get' makes the actual HTTP GET request to the API.
        response = requests.get(endpoint, headers=headers, params=params)
        # '.raise_for_status()' checks if the request was successful (status code 200).
        # If it wasn't, it raises an exception, which is caught below.
        response.raise_for_status()
        # '.json()' parses the JSON response from the API into a Python dictionary.
        data = response.json()

        # Check for empty or missing data in the response.
        if not data.get('response') or not data['response'][0]['league']['standings']:
            return {"error": "No standings found for this league and season."}

        # Extract the standings data from the API's complex JSON structure.
        standings = data['response'][0]['league']['standings'][0]

        # Reformat the data into a cleaner, more readable format for the LLM.
        formatted_standings = [
            {
                "rank": team['rank'],
                "team": team['team']['name'],
                "points": team['points'],
                "games_played": team['all']['played'],
                "wins": team['all']['win'],
                "draws": team['all']['draw'],
                "losses": team['all']['lose'],
            }
            for team in standings
        ]

        return formatted_standings

    # Catch any exceptions that happen during the request (e.g., network error, bad API key).
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}

# This is a list of all your custom tools.
# You will add more functions to this list as you create them.
CUSTOM_TOOLS = [get_league_standings]
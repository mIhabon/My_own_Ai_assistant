import logging
import requests
from livekit.agents import function_tool, RunContext
from langchain_community.tools import DuckDuckGoSearchRun

@function_tool()
async def get_weather(context: RunContext, city: str) -> str:
    """Get current weather for Ihab's location"""
    try:
        response = requests.get(f"https://wttr.in/{city}?format=3")
        if response.status_code == 200:
            return response.text.strip()
        return f"Could not retrieve weather for {city}."
    except Exception as e:
        return f"Weather service unavailable: {str(e)}"

@function_tool()
async def search_web(context: RunContext, query: str) -> str:
    """Search the web for Ihab"""
    try:
        results = DuckDuckGoSearchRun().run(tool_input=query)
        return results
    except Exception as e:
        return f"Search failed: {str(e)}"
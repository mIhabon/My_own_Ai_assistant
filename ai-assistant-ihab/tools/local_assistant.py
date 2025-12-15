# local_assistant.py - Local version without LiveKit
import asyncio
import json
from tools.web_tools import get_weather, search_web
from tools.system_tools import open_application
from tools.communication_tools import send_email
from memory.enhanced_memory import EnhancedMemoryClient
from config.settings import load_config
import os

config = load_config()

class LocalAssistant:
    def __init__(self):
        self.memory = EnhancedMemoryClient(api_key=os.getenv("MEM0_API_KEY"))
        self.tools = {
            "weather": get_weather,
            "search": search_web,
            "open_app": open_application,
            "send_email": send_email
        }
    
    async def process_command(self, command: str):
        """Process user commands locally"""
        command = command.lower()
        
        if "weather" in command:
            # Extract city name
            if "in" in command:
                city = command.split("in")[-1].strip()
            else:
                city = "London"  # default
            return await self.tools["weather"](None, city)
        
        elif "search" in command or "look up" in command:
            query = command.replace("search", "").replace("look up", "").strip()
            return await self.tools["search"](None, query)
        
        elif "open" in command:
            app_name = command.replace("open", "").strip()
            return await self.tools["open_app"](None, app_name)
        
        elif "email" in command or "send" in command:
            return "Email functionality requires Gmail setup. Update your .env file with real credentials."
        
        else:
            return "I can help you with: weather, search, open apps, or send emails. Try something like 'weather in Paris' or 'open notepad'."

async def main():
    assistant = LocalAssistant()
    print("🤖 Friday AI Assistant (Local Mode)")
    print("Commands: weather, search, open, email")
    print("Type 'quit' to exit\n")
    
    while True:
        try:
            user_input = input("Ihab: ").strip()
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Goodbye Ihab! 👋")
                break
            
            if user_input:
                response = await assistant.process_command(user_input)
                print(f"Friday: {response}\n")
                
        except KeyboardInterrupt:
            print("\nGoodbye Ihab! 👋")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
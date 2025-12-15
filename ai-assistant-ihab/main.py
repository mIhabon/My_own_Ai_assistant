from agents.assistant import entrypoint
from dotenv import load_dotenv
import logging

if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    print("🚀 Starting Ihab's AI Assistant...")
    
    # This will start the LiveKit worker
    # You need to run this with LiveKit CLI
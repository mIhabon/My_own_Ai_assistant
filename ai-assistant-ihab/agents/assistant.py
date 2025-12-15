from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions, ChatContext
from livekit.plugins import noise_cancellation, google
from config.prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION
from tools.web_tools import get_weather, search_web
from tools.communication_tools import send_email
from tools.system_tools import open_application
from memory.enhanced_memory import EnhancedMemoryClient
from config.settings import load_config
import logging
import asyncio
import os

load_dotenv()
config = load_config()

class Assistant(Agent):
    def __init__(self, chat_ctx=None) -> None:
        super().__init__(
            instructions=AGENT_INSTRUCTION,
            llm=google.beta.realtime.RealtimeModel(voice=config.VOICE_MODEL),
            tools=[get_weather, search_web, send_email, open_application],
            chat_ctx=chat_ctx
        )

async def entrypoint(ctx: agents.JobContext):
    # Initialize components
    memory = EnhancedMemoryClient(api_key=os.getenv("MEM0_API_KEY"))
    session = AgentSession()
    
    try:
        # Start session
        await session.start(
            room=ctx.room,
            agent=Assistant(),
            room_input_options=RoomInputOptions(
                video_enabled=True,
                noise_cancellation=noise_cancellation.BVC(),
            ),
        )

        await ctx.connect()
        await session.generate_reply(instructions=SESSION_INSTRUCTION)
        await asyncio.Future()  # Run forever
        
    except Exception as e:
        logging.error(f"Session error: {e}")
        raise

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
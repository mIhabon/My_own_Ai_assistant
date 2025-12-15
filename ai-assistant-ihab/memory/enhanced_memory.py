from mem0 import AsyncMemoryClient
from datetime import datetime, timezone
import logging
from typing import List, Dict, Any
from config.settings import AssistantConfig

config = AssistantConfig()

class EnhancedMemoryClient(AsyncMemoryClient):
    async def get_contextual_memories(self, current_conversation: str, max_memories: int = 5) -> List[Dict]:
        """Get relevant memories for Ihab"""
        try:
            results = await self.search(current_conversation, user_id=config.USER_NAME)
            return sorted(results, key=lambda x: x.get('updated_at', ''), reverse=True)[:max_memories]
        except Exception as e:
            logging.error(f"Memory search failed: {e}")
            return []
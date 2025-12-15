import os
from dataclasses import dataclass

@dataclass
class AssistantConfig:
    USER_NAME: str = "Ihab"
    VOICE_MODEL: str = "Aoede"
    MAX_MEMORIES: int = 10
    ALLOWED_APPS: list = None
    
    def __post_init__(self):
        if self.ALLOWED_APPS is None:
            self.ALLOWED_APPS = ["notepad", "calculator", "chrome", "spotify", "vscode", "terminal"]

def load_config() -> AssistantConfig:
    return AssistantConfig(
        USER_NAME=os.getenv("USER_NAME", "Ihab"),
        VOICE_MODEL=os.getenv("VOICE_MODEL", "Aoede"),
        MAX_MEMORIES=int(os.getenv("MAX_MEMORIES", "10"))
    )
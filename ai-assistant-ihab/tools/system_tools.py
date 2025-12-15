import logging
import subprocess
import platform
from livekit.agents import function_tool, RunContext
from config.settings import AssistantConfig

config = AssistantConfig()

@function_tool()
async def open_application(context: RunContext, app_name: str) -> str:
    """Open applications for Ihab"""
    if app_name.lower() not in [app.lower() for app in config.ALLOWED_APPS]:
        return f"Sorry Ihab, I can't open {app_name} for security reasons."
    
    system = platform.system()
    app_commands = {
        "windows": {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "chrome": "start chrome",
            "spotify": "spotify.exe",
            "vscode": "code",
            "terminal": "cmd.exe"
        },
        "darwin": {
            "notepad": "open -a TextEdit",
            "calculator": "open -a Calculator",
            "chrome": "open -a 'Google Chrome'",
            "spotify": "open -a Spotify",
            "vscode": "open -a 'Visual Studio Code'",
            "terminal": "open -a Terminal"
        },
        "linux": {
            "notepad": "gedit",
            "calculator": "gnome-calculator",
            "chrome": "google-chrome",
            "spotify": "spotify",
            "vscode": "code",
            "terminal": "gnome-terminal"
        }
    }
    
    try:
        system_key = "windows" if system == "Windows" else "darwin" if system == "Darwin" else "linux"
        command = app_commands[system_key][app_name.lower()]
        subprocess.Popen(command, shell=True)
        return f"Opened {app_name} for you, Ihab."
    except Exception as e:
        return f"Couldn't open {app_name}: {str(e)}"
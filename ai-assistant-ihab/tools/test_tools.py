# test_tools.py - Test all tools
import asyncio
from tools.web_tools import get_weather, search_web
from tools.system_tools import open_application

async def test_all_tools():
    print("🧪 Testing All Tools...")
    
    # Test 1: Weather
    print("\n1. 🌤️ Testing Weather:")
    weather = await get_weather(None, "Paris")
    print(f"   Result: {weather}")
    
    # Test 2: Search
    print("\n2. 🔍 Testing Search:")
    search = await search_web(None, "latest technology news")
    print(f"   Result: {search[:200]}...")
    
    # Test 3: Open App
    print("\n3. 🖥️ Testing App Opening:")
    try:
        app_result = await open_application(None, "notepad")
        print(f"   Result: {app_result}")
    except Exception as e:
        print(f"   Error: {e} (might be expected on some systems)")
    
    print("\n✅ All tests completed!")

if __name__ == "__main__":
    asyncio.run(test_all_tools())
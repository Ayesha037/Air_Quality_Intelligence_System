import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.waqi.info/feed"

cities_str = os.getenv("CITIES", "delhi,mumbai,bangalore")
CITIES = [city.strip() for city in cities_str.split(",")]

if API_KEY:
    print(f"✅ API Key loaded: {API_KEY[:20]}...")
else:
    print("❌ No API Key found in .env file!")

print(f"✅ Loaded {len(CITIES)} cities")
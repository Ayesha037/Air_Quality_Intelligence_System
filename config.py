import os
from dotenv import load_dotenv
import streamlit as st

try:
    API_KEY = st.secrets["API_KEY"]
    cities_str = st.secrets.get("CITIES", "delhi,mumbai,bangalore")
except:
  
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    cities_str = os.getenv("CITIES", "delhi,mumbai,bangalore")

BASE_URL = "https://api.waqi.info/feed"

CITIES = [city.strip() for city in cities_str.split(",")]

print(f"✅ API Key loaded")
print(f"✅ Loaded {len(CITIES)} cities")
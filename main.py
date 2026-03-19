import firebase_admin
from firebase_admin import credentials, firestore
import requests
from weather import weather_report 
from news_engine import news_report
import os

print("Initializing Firebase...")

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

print("Firebase initialized.")

def send_to_telegram(chat_id, message): 
    BOT_TOKEN = os.getenv("TELEGRAM_API")

    if not BOT_TOKEN:
        print("❌ TELEGRAM_API is missing!")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": chat_id,
        "text": message,
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        print(f"Telegram response: {response.status_code}")
    except Exception as e:
        print(f"Telegram error: {e}")

def send_all_updates():
    print("Starting update process...")

    docs = db.collection("users").stream() 

    for doc in docs:
        print(f"Processing user: {doc.id}")
        user_data = doc.to_dict()
        
        target_id = user_data.get("telegramId")
        cities = user_data.get("cities", [])
        countries = user_data.get("countries", [])

        weather_info = ""

        for city in cities:
            print(f"Getting weather for {city}")
            try:
                weather_info += weather_report(city) + "\n"
            except Exception as e:
                print(f"Weather error: {e}")

        print("Getting news...")
        try:
            news_info = news_report(countries)
        except Exception as e:
            print(f"News error: {e}")
            news_info = "Error fetching news."

        full_msg = f"Hello! Here is your update:\n\n{weather_info}\n\n{news_info}"
        
        if target_id:
            print(f"Sending message to {target_id}")
            send_to_telegram(target_id, full_msg)
        else:
            print(f"Missing Telegram ID for {doc.id}")

if __name__ == "__main__":
    send_all_updates()

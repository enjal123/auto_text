import firebase_admin
from firebase_admin import credentials, firestore
import requests
from weather import weather_report 
from news_engine import news_report
import os

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def send_to_telegram(chat_id, message): 
    BOT_TOKEN = os.getenv("TELEGRAM_API")
    chat_id = os.getenv("TELEGRAM")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": chat_id,
        "text": message,  
    }
    
    response = requests.post(url, json=payload)
    return response.status_code

def send_all_updates():
    docs = db.collection("users").stream() 

    for doc in docs:
        user_data = doc.to_dict()
        
        target_id = user_data.get("telegramId")
        cities = user_data.get("cities", [])
        countries = user_data.get("countries", [])

        weather_info = ""
        for city in cities:
            weather_info += weather_report(city) +"\n"
            
        news_info = news_report(countries)
        
        full_msg = f"Hello! Here is your update:\n\n{weather_info}\n\n{news_info}"
        
        if target_id:
            send_to_telegram(target_id, full_msg)
        else:
            print(f"User {doc.id} is missing a Telegram ID.")

if __name__ == "__main__":
    send_all_updates()

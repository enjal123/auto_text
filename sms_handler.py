import requests
from weather import weather_report   
from news_engine import news_report  
import os

def send_sms(city):
    
    current_weather = weather_report(city)
    current_news = news_report()

    full_message = f"Daily Update\n\n{current_weather}\n\n{current_news}"

    API = os.getenv("TELEGRAM_API")
    ID = os.getenv("TELEGRAM_ID")
    url = f"https://api.telegram.org/bot{API}/sendMessage"

    payload = {
        "chat_id": ID,
        "text": full_message,
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Update sent successfully!")
    else:
        print(f"Error: {response.status_code}")
        print(f"Error: {response.status_code} - {response.text}")


if __name__ == "__main__":
    send_sms()

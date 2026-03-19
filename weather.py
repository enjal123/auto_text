from pyowm import OWM
from geopy.geocoders import ArcGIS
import datetime
import os 
def weather_report(user_location):
    api_key = os.getenv("WEATHER_API_KEY")
    owm = OWM(api_key)
    geolocator = ArcGIS()

    if user_location:
        location = geolocator.geocode(user_location)
    
        if location:
            lat = location.latitude
            lon = location.longitude

            observation = owm.weather_manager().weather_at_coords(lat, lon)
            w = observation.weather
        
            temp = w.temperature(unit="fahrenheit")['temp']
            weather_status = w.status
            detailed_weather_status = w.detailed_status
            rain_volume = w.rain.get('1h', 0)
            wind_speed = w.wind().get('speed', 0)
        
            clouds = w.clouds
            visibility = w.visibility_distance
            sunrise = datetime.datetime.fromtimestamp(w.sunrise_time()).strftime('%I:%M %p')
            sunset = datetime.datetime.fromtimestamp(w.sunset_time()).strftime('%I:%M %p')

            report = f"\n--- 🌤 WEATHER REPORT ---\n"
            report += f"📍 Location: {location.address}\n"
            report += f"🌡 Temp: {temp}°F\n"
            report += f"☁️ Sky: {weather_status} ({detailed_weather_status})\n"
            report += f"💨 Wind Speed: {wind_speed} m/s\n"
        
            if rain_volume > 0:
                report += f"🌧 Rain Volume: {rain_volume} mm\n"
            else:
                report += "☀️ Precipitation: None\n"
            
            report += f"🌅 Sunrise: {sunrise}\n"
            report += f"🌇 Sunset: {sunset}\n"
            report += "-" * 20

            return report
            
    return "❌ Error: Could not find that location."


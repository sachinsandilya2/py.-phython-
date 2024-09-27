import requests
from twilio.rest import Client
import schedule
import time
from instabot import Bot

# Twilio Credentials
account_sid = 'MGeba305642336b821c8f357fb588a35b2'  # Replace with your Twilio SID
auth_token = '5d7379f7ba5ba6e91ca2c61e4f721d89'  # Replace with your Twilio Auth Token
client = Client(account_sid, auth_token)

# OpenWeatherMap API Key
weather_api_key = '2aa27409fb729f0fb4155ac2fa6b4d54'

# Instagram credentials (replace with your own)
instagram_username = 'your_instagram_username'
instagram_password = 'your_instagram_password'
bot = Bot()

# Login to Instagram
bot.login(username=instagram_username, password=instagram_password)

# Function to get weather information for a city
def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        description = weather['description']
        return f"Current temperature: {temperature}°C\nWeather condition: {description}"
    else:
        return "City Not Found!"

# Function to select song based on weather condition
def get_weather_based_song(weather_condition):
    if 'rain' in weather_condition.lower():
        return 'https://www.youtube.com/watch?v=NUsoVlDFqZg'  # Rainy song link (Fix You - Coldplay)
    elif 'clear' in weather_condition.lower():
        return 'https://www.youtube.com/watch?v=PT2_F-1esPk'  # Sunny song link (Shape of You - Ed Sheeran)
    elif 'cloud' in weather_condition.lower():
        return 'https://www.youtube.com/watch?v=RgKAFK5djSk'  # Cloudy song link (See You Again - Wiz Khalifa)
    else:
        return 'https://www.youtube.com/watch?v=LsoLEjrDogU'  # Default song link (Something Just Like This - Chainsmokers)

# Function to send WhatsApp message
def send_whatsapp_message(to_number, city):
    weather_info = get_weather(city)
    song_link = get_weather_based_song(weather_info)
    
    message = f"Hello! Here's the weather update for {city}:\n{weather_info}\nEnjoy this month's song: {song_link}"
    
    client.messages.create(
        from_='whatsapp:+917256932133',  # Twilio sandbox WhatsApp number
        body=message,
        to=f'whatsapp:{to_number}'
    )
    print(f"WhatsApp message sent to {to_number}")

# Function to send Instagram message
def send_instagram_message(username, city):
    weather_info = get_weather(city)
    song_link = get_weather_based_song(weather_info)
    
    message = f"Hey! Here's the weather update for {city}:\n{weather_info}\nCheck out this month's song: {song_link}"
    
    bot.send_message(message, [username])
    print(f"Instagram message sent to {username}")

# Function to schedule monthly messages
def schedule_monthly_messages(

):
    friends = [
        {'number': '+91891763456', 'city': 'Delhi', 'instagram': 'friend1_instagram_username'},
        {'number': '+918002423541', 'city': 'Mumbai', 'instagram': 'friend2_instagram_username'}
    ]
    
    for friend in friends:
        # Send WhatsApp message
        send_whatsapp_message(friend['number'], friend['city'])
        # Send Instagram message
        send_instagram_message(friend['_searching_for_happiness_5'], friend['bihar'])

# Schedule the message to be sent on the 1st of every month at 10:00 AM
schedule.every().month.at("10:00").do(schedule_monthly_messages)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)

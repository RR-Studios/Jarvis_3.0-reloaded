import pyttsx3
import requests

#speak function
engine = pyttsx3.init('sapi5')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Function to get the live weather
def get_live_location_weather(api_key):
    try:
        # Get the user's IP address-based location
        response = requests.get("https://ipinfo.io")
        data = response.json()

        # Extract the city from the location data
        city = data.get("city")

        if city:
            # Request weather information for the detected city
            weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
            response=  requests.get(weather_url)
            weather_data = response.json()

            if 'main' in weather_data and 'weather' in weather_data:
                temperature = weather_data['main']['temp']
                description = weather_data['weather'][0]['description']
                return f"The weather in {city} is {description} with a temperature of {temperature}°C."
            else:
                return "Weather data not found for the current location."

        return "Unable to determine the user's location."

    except Exception as e:
        print(str(e))
        return "Error while determining the user's location or fetching weather data."
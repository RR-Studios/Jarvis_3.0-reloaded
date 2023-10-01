import requests
from geopy.geocoders import Nominatim


def get_live_location(api_key):
    try:
        # Get the user's IP address-based location
        response = requests.get("https://ipinfo.io")
        data = response.json()

        # Extract the city from the location data
        city = data.get("city")

        if city:
            # Request weather information for the detected city
            weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
            response = requests.get(weather_url)
            weather_data = response.json()

            if 'main' in weather_data and 'weather' in weather_data:
                temperature = weather_data['main']['temp']
                description = weather_data['weather'][0]['description']
                return city, description, temperature
            else:
                return "Location data not found."

        return "Unable to determine the user's location."

    except Exception as e:
        print(str(e))
        return "Error while determining the user's location or fetching weather data."


def get_directions(origin, destination, api_key):
    try:
        geolocator = Nominatim(user_agent="route_info")
        origin_location = geolocator.geocode(origin)
        destination_location = geolocator.geocode(destination)

        if origin_location and destination_location:
            origin_coords = f"{origin_location.latitude},{origin_location.longitude}"
            destination_coords = f"{destination_location.latitude},{destination_location.longitude}"

            base_url = "https://maps.googleapis.com/maps/api/directions/json"

            params = {
                "origin": origin_coords,
                "destination": destination_coords,
                "key": api_key,
            }

            response = requests.get(base_url, params=params)
            data = response.json()

            if 'routes' in data and data['routes']:
                best_route = data['routes'][0]
                duration = best_route['legs'][0]['duration']['text']
                distance = best_route['legs'][0]['distance']['text']
                steps = best_route['legs'][0]['steps']

                instructions = []
                for step in steps:
                    instructions.append(step['html_instructions'])

                return f"Here are the directions from {origin} to {destination}:\nDuration: {duration}\nDistance: {distance}\nInstructions: {', '.join(instructions)}"

            else:
                return "Directions not found."

        return "Origin or destination not found."

    except Exception as e:
        print(str(e))
        return "Error while fetching directions."


# Example usage:
# Replace 'YOUR_WEATHER_API_KEY' and 'YOUR_GOOGLE_MAPS_API_KEY' with your actual API keys
if __name__ == "__main__":
    weather_api_key = 'YOUR_WEATHER_API_KEY'
    maps_api_key = 'YOUR_GOOGLE_MAPS_API_KEY'

    city, description, temperature = get_live_location(weather_api_key)
    print(f"The weather in {city} is {description} with a temperature of {temperature}°C.")

    origin = "New York"
    destination = "Los Angeles"
    directions = get_directions(origin, destination, maps_api_key)
    print(directions)

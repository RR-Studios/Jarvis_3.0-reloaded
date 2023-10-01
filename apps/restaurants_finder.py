import requests
from geopy.geocoders import Nominatim


def find_restaurants_near_me(api_key):
    try:
        # Get the user's IP address-based location
        response = requests.get("https://ipinfo.io")
        data = response.json()

        # Extract the city from the location data
        city = data.get("city")

        if city:
            # Initialize a geolocator
            geolocator = Nominatim(user_agent="restaurant_finder")

            # Find the coordinates (latitude and longitude) of the city
            location = geolocator.geocode(city)

            if location:
                latitude = location.latitude
                longitude = location.longitude

                # Use the coordinates to search for restaurants
                search_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
                params = {
                    "location": f"{latitude},{longitude}",
                    "radius": 1000,  # Adjust the radius as needed
                    "keyword": "restaurant",  # Change to your preferred keyword
                    "key": api_key
                }

                response = requests.get(search_url, params=params)
                results = response.json()

                if 'results' in results:
                    # Extract restaurant names and addresses
                    restaurants = [(place['name'], place['vicinity']) for place in results['results']]
                    return restaurants
                else:
                    return "No restaurants found near your location."

        return "Unable to determine the user's location."

    except Exception as e:
        print(str(e))
        return "Error while determining the user's location or fetching restaurant data."

import requests
import os

def get_temperature(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': f'{city},US',
        'appid': api_key,
        'units': 'imperial'  # You can change this to 'metric' for Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        temperature = data['main']['temp']
        return temperature
    except requests.RequestException as e:
        print(f"Failed to get temperature data for {city}. Error: {e}")
        return None

def compare_temperatures(api_key, target_city, cities_to_compare, temperature_range=5):
    target_temperature = get_temperature(api_key, target_city)

    if target_temperature is not None:
        matching_cities = []

        for city in cities_to_compare:
            city_temperature = get_temperature(api_key, city)

            if city_temperature is not None and abs(city_temperature - target_temperature) < temperature_range:
                matching_cities.append(city)

        return matching_cities
    else:
        return None

if __name__ == "__main__":
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    
    if api_key is None:
        print("API key not found. Please set the OPENWEATHERMAP_API_KEY environment variable.")
    else:
        target_city = 'San Jose'
        cities_to_compare = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'Dallas', 'Austin', 'Portland', 'Naselle', 'Orlando']

        matching_cities = compare_temperatures(api_key, target_city, cities_to_compare)

        if matching_cities is not None:
            print(f"Cities with similar temperatures to {target_city}: {matching_cities}")
        else:
            print("Failed to retrieve data.")
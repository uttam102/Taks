import requests

def get_weather(city_name, api_key):
    """
    Fetch weather data for a given city using OpenWeatherMap API.
    
    Args:
        city_name (str): Name of the city
        api_key (str): API key for OpenWeatherMap
        
    Returns:
        dict: Weather data or None if request fails
    """     
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric' 
    }
    
    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        
        # Check if request was successful
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"\nCity '{city_name}' not found!")
            return None
        elif response.status_code == 401:
            print("\nInvalid API key! Please check your API key.")
            return None
        else:
            print(f"\nError: Unable to fetch weather data (Status code: {response.status_code})")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"\nNetwork error: {e}")
        return None


def display_weather(weather_data):
    """
    Display weather information in a user-friendly format.
    
    Args:
        weather_data (dict): Weather data from API
    """
    if not weather_data:
        return
    
    # Extract relevant information from JSON data
    city = weather_data['name']
    country = weather_data['sys']['country']
    temperature = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']
    weather_condition = weather_data['weather'][0]['description']
    wind_speed = weather_data['wind']['speed']
    
    # Display weather information
    print("\n" + "=" * 50)
    print(f"WEATHER IN {city.upper()}, {country}")
    print("=" * 50)
    print(f"Condition:       {weather_condition.title()}")
    print(f"Temperature:     {temperature}°C")
    print(f"Feels Like:      {feels_like}°C")
    print(f"Humidity:        {humidity}%")
    print(f"Pressure:        {pressure} hPa")
    print(f"Wind Speed:      {wind_speed} m/s")
    print("=" * 50)


def main():
    """
    Main function to run the weather app.
    """
    print("\n" + "=" * 50)
    print("WEATHER APP")
    print("=" * 50)
    
    # Users should replace this with their own API key
    # Example: api_key = "abc123def456ghi789"  (just the key, not the full URL)
    api_key = "4c48e410f4d6c68702832ba3ca46f15f"
    
    try:
        while True:
            city = input("\nEnter city name (or 'quit' to exit): ").strip()
            if city.lower() == 'quit':
                print("\nThank you for using Weather App! Goodbye!")
                break
            if not city:
                print("Please enter a valid city name!")
                continue
            weather_data = get_weather(city, api_key)
            display_weather(weather_data)
    except (KeyboardInterrupt, EOFError):
        print("\n\nThank you for using Weather App! Goodbye!")

if __name__ == "__main__":
    main()
    
    

import requests

# Replace with your actual OpenWeatherMap API key
API_KEY = '9c17c19df8585b055938e95fb917fc94'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city_name):
    complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(complete_url)
    if response.status_code == 200:
        weather_data = response.json()
        main_data = weather_data['main']
        temperature = main_data['temp']
        pressure = main_data['pressure']
        humidity = main_data['humidity']
        weather_desc = weather_data['weather'][0]['description']
        print(f"City: {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {weather_desc}")
    else:
        # If there was an error in the request
        print("Error fetching weather data.")

city_name = input("Enter city name: ")
get_weather(city_name)
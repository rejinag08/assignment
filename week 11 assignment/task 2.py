import requests
def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15
def get_weather(Municipality):
    api_key = "cd7e9eaf217aef78b1d4f60985a71f6e"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        if response.status_code ==200:
            data = response.json()
            weather = data['weather'][0]['description']
            temp_celsius = kelvin_to_celsius(data['main']['temp'])

        print(f"Weather in {city.capitalize()}: {weather.capitalize()}")
        print(f"Temperature: {temp_celsius:.2f}°C")
    except Exception as e:
        print("Error fetching weather data. Please try again.")
city = input("Enter a Municipality name: ").strip()
get_weather(Municipality=city)
#
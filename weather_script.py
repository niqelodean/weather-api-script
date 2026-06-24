import requests

try:
    city_name = input("Enter City Name: ")
    response = requests.get(f"https://wttr.in/{city_name}?format=j1")
    data = response.json()

    temp_c = data["current_condition"][0]["temp_C"]
    humidity = data["current_condition"][0]["humidity"]
    weather_desc = data["current_condition"][0]["weatherDesc"][0]["value"]

    print(f"Temperature in {city_name}: {temp_c}°C")
    print(f"Humidity in {city_name}: {humidity}")
    print(f"Weather in {city_name}: {weather_desc}")

except (requests.exceptions.RequestException, ValueError, KeyError, IndexError) as e:
    print(f"Error retrieving or parsing data: {e}")

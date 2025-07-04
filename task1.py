import requests
import matplotlib.pyplot as plt

# my API key
api_key = "7346d0602f87939a3ccf655e4106bdf0"

# Input city name
city = input("Enter city name: ")

# OpenWeather API endpoint
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")

        # Data visualization
        labels = ['Temperature (°C)', 'Humidity (%)']
        values = [temperature, humidity]
        colors = ['skyblue', 'lightgreen']

        plt.bar(labels, values, color=colors)
        plt.title(f"Weather Stats for {city.title()}")
        plt.ylabel('Values')
        plt.show()

    else:
        print(f"Error: {data['message']}")

except Exception as e:
    print("Something went wrong:",e)

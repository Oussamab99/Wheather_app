
import requests

# Get the weather information
def getWeather(api_key,city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    #print(data)
    return data

# Display the weather information
def displayWeather(data):
    if data["cod"] != "404":
        print(f"Weather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Description: {data['weather'][0]['description']}")
    else:
        print("City not found.")

# Main function
def main():
    api_key = "172d7ddf61d72b662c887e5a0b234d07"
    city = input("Enter a city: ")
    Whether = getWeather(api_key,city)
    displayWeather(Whether)

if __name__ == "__main__":
    main()






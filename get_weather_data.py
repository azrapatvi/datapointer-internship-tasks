import requests #type:ignore

city_name = input("enter city:")
API_key = "YOUR_API_KEY"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data=response.json()
    print("weather is:",data['weather'][0]['description'])
    print("current temprature is:",data['main']['temp'])
    print("current temprature feels like is:",data['main']['feels_like'])
    print("humidity is:",data['main']['humidity'])
else:
    print("Something went wrong.")


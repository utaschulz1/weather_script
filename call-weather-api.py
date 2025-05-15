import os
import requests
from openai import OpenAI
from llm_abfrage import print_llm_response, get_llm_response # functions in file llm-abfrage.py
from dotenv import load_dotenv
from opencage.geocoder import OpenCageGeocode
import requests

#load environment variables from the .env file
load_dotenv('.env', override=True)
# Get API keys from the environment
opencage_api_key = os.getenv("OPENCAGE_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")


# Initialize the OpenCage Geocoder
geocoder = OpenCageGeocode(opencage_api_key)

# City name to query
city_name = input("Enter the name of the city (e.g. Berlin, Germany): ")

# Get latitude and longitude for the city from OpenCage Geocoder API
result = geocoder.geocode(city_name)
if result and len(result) > 0:
    latitude = result[0]['geometry']['lat']
    longitude = result[0]['geometry']['lng']
    print(f"Latitude: {latitude}, Longitude: {longitude}")

    # Use Open-Meteo API (no API key) with the obtained latitude and longitude
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    # Use the get function from the requests library to store the response from the API
    response = requests.get(url)
    # Take the response from the API (in JSON) and assign it to a Python dictionary
    weather_data = response.json()
    # Print the weather data (for debugging, otherwise return)
    print(weather_data) # result is a dictionary:
# {'cod': '200', 'message': 0, 'cnt': 1, 'list': [{'dt': 1723831200, 'main': {'temp': 34.14, 'feels_like': 23.94, 'temp_min': 22.84, 'temp_max': 24.02, 'pressure': 1017, 'sea_level': 1017, 'grnd_level': 949, 'humidity': 56, 'temp_kf': 1.15}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.18, 'deg': 191, 'gust': 3.83}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-08-16 18:00:00'}], 'city': {'id': 5518301, 'name': 'Carey', 'coord': {'lat': 34.38, 'lon': -100.36}, 'country': 'US', 'population': 0, 'timezone': -18000, 'sunrise': 1723809821, 'sunset': 1723858068}

else:
    print("City not found.")

#Initilize the OpenAI Client
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Function to interpret the weather code
def interpret_weather_code(code):
    if code == 0:
        return "Clear sky"
    elif code in [1, 2, 3]:
        return "Mainly clear, partly cloudy, and overcast"
    elif code in [45, 48]:
        return "Fog and depositing rime fog"
    elif code in [51, 53, 55]:
        return "Drizzle: Light, moderate, and dense intensity"
    elif code in [56, 57]:
        return "Freezing Drizzle: Light and dense intensity"
    elif code in [61, 63, 65]:
        return "Rain: Slight, moderate, and heavy intensity"
    elif code in [66, 67]:
        return "Freezing Rain: Light and heavy intensity"
    elif code in [71, 73, 75]:
        return "Snow fall: Slight, moderate, and heavy intensity"
    elif code == 77:
        return "Snow grains"
    elif code in [80, 81, 82]:
        return "Rain showers: Slight, moderate, and violent"
    elif code in [85, 86]:
        return "Snow showers: Slight and heavy"
    elif code == 95:
        return "Thunderstorm: Slight or moderate"
    elif code in [96, 99]:
        return "Thunderstorm with slight and heavy hail"
    else:
        return "Unknown weather code"

# Extracting the relevant data
temperature = weather_data['current_weather']['temperature']
windspeed = weather_data['current_weather']['windspeed']
winddirection = weather_data['current_weather']['winddirection']
weathercode = weather_data['current_weather']['weathercode']

# Interpreting the weather code
weather_description = interpret_weather_code(weathercode)

# Printing the extracted data
print(f"Temperature: {temperature} °C")
print(f"Wind Speed: {windspeed} km/h")
print(f"Wind Direction: {winddirection}°")
print(f"Weather Code: {weathercode} - {weather_description}")

weather_string = f"""The temperature in {city_name} is {temperature}°C. 
It is currently {weather_description},
with a wind speed of {windspeed}m/s.
"""

print(weather_string)

prompt = f"""Based on the following weather, 
suggest an appropriate outdoor outfit.

Forecast: {weather_string}
"""


# Print the LLM response
print_llm_response(prompt)

# Generate the LLM response
response = get_llm_response(prompt)
print(f"Type of response: {type(response)}")  # Should print <class 'str' (for debugging)>

# Save weather_string and response to a Markdown file
def save_response_to_md(response, filename="weather_response.md"):
    """Save the response to a Markdown file."""
    try:
        with open(filename, "w", encoding="utf-8") as md_file:
            md_file.write("# Weather Forecast\n\n")
            md_file.write(f"## Weather Details\n\n{weather_string}\n\n")
            md_file.write("## Suggested Outfit\n\n")
            md_file.write(response)
        print(f"Response saved to {filename}")
    except Exception as e:
        print(f"Error saving response to file: {e}")

# Call: Save the weather_string and response to a Markdown file
save_response_to_md(response)
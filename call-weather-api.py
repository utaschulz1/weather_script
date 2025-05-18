import os
from dotenv import load_dotenv
from llm_utils import get_llm_response, print_llm_response
from weather_utils import get_coordinates, fetch_weather_data, interpret_weather_code

# Load environment variables
load_dotenv('.env', override=True)

print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")

def save_response_to_md(weather_string, llm_response, filename="weather_response.md"):
    """Save the weather and LLM response to a Markdown file."""
    try:
        with open(filename, "w", encoding="utf-8") as md_file:
            md_file.write("# Weather Forecast\n\n")
            md_file.write(f"## Weather Details\n\n{weather_string}\n\n")
            md_file.write("## Suggested Outfit\n\n")
            md_file.write(llm_response)
        print(f"Response saved to {filename}")
    except Exception as e:
        print(f"Error saving response to file: {e}")

def main():
    city_name = input("Enter the name of the city (e.g., Berlin, Germany): ")
    latitude, longitude = get_coordinates(city_name)

    if latitude is None or longitude is None:
        return

    weather_data = fetch_weather_data(latitude, longitude)
    if weather_data is None:
        return

    current_weather = weather_data['current_weather']
    temperature = current_weather['temperature']
    windspeed = current_weather['windspeed']
    winddirection = current_weather['winddirection']
    weathercode = current_weather['weathercode']
    weather_description = interpret_weather_code(weathercode)

    weather_string = (
        f"The temperature in {city_name} is {temperature}°C. "
        f"It is currently {weather_description}, "
        f"with a wind speed of {windspeed} m/s."
    )
    print(weather_string)

    prompt = f"Based on the following weather, suggest an appropriate outdoor outfit.\n\nForecast: {weather_string}"
    llm_response = get_llm_response(prompt)

    save_response_to_md(weather_string, llm_response)

if __name__ == "__main__":
    main()
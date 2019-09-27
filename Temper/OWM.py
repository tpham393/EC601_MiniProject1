import pyowm

# Uses OWM API to retrieve and return current Boston weather
# Stores pertinent components of weather information in an object for easy access/manipulation
# Better organization than returning tuple with many values
class weather:
    def __init__(self):
        api_key = input("Please input API key: ")
        owm = pyowm.OWM(api_key)  # You MUST provide a valid API key

        # Search for current weather in Boston (US) -- must specify ISO 3166 country code
        city = input("Please input a US city")
        
        observation = owm.weather_at_place(city + ', US')

        if ( observation is not None ):
            w = observation.get_weather()
            # Weather details
            self.wind_speed = w.get_wind()['speed']           # returns dictionary with keys: 'speed', 'deg'
            self.humidity = w.get_humidity()                  # 87
            
            temperature = w.get_temperature('fahrenheit')     # returns a dictionary with keys: 'temp_max', 'temp', and 'temp_min'
            self.temp_max = temperature['temp_max']
            self.temp_current = temperature['temp']
            self.temp_min = temperature['temp_min']
            
            self.status = w.get_status()
            self.detailed_status = w.get_detailed_status()
        
        # error handling -- user enters invalid US city
        else:
            print("You have entered an invalid city. Returning the weather information for Boston...")
            observation = owm.weather_at_place('Boston, US')
            w = observation.get_weather()
            # Weather details
            self.wind_speed = w.get_wind()['speed']           # returns dictionary with keys: 'speed', 'deg'
            self.humidity = w.get_humidity()                  # 87
            
            temperature = w.get_temperature('fahrenheit')     # returns a dictionary with keys: 'temp_max', 'temp', and 'temp_min'
            self.temp_max = temperature['temp_max']
            self.temp_current = temperature['temp']
            self.temp_min = temperature['temp_min']
            
            self.status = w.get_status()
            self.detailed_status = w.get_detailed_status()

def get_weather():
    return weather()

# Test code for above method
print('----- TESTING OWM MODULE -----')
w = get_weather()
print("Wind speed: ", w.wind_speed)
print("Humidity: ", w.humidity)
print("High (F): ", w.temp_max)
print("Current temp (F): ", w.temp_current)
print("Low (F): ", w.temp_min)
print("Status (F): ", w.status)
print("Detailed status (F): ", w.detailed_status)
print('----- END TEST OWM MODULE -----')
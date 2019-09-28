import pyowm

# Uses OWM API to retrieve and return current Boston weather
# Stores pertinent components of weather information in an object for easy access/manipulation
# Better organization than returning tuple with many values
class weather:
    def __init__(self, wind_speed=None, humidity=None, temp_max=None, temp_current=None, temp_min=None, status=None, detailed_status=None): 
        self.wind_speed = wind_speed
        self.humidity = humidity
        self.temp_max = temp_max
        self.temp_current = temp_current
        self.temp_min = temp_min
        self.status = status
        self.detailed_status = detailed_status

    # Class Method to display weather details used to determine sentiment label,
    # i.e. temp_current and status
    def display_weather(self):
        print( 'Current temperature: ', self.temp_current, ', Status: ', self.status )

# Method to retrieve the weather object
def get_weather():
    api_key = input("Please input API key: ")
    owm = pyowm.OWM(api_key)  # You MUST provide a valid API key

    try:
        # Search for current weather in Boston (US) -- must specify ISO 3166 country code
<<<<<<< HEAD
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
=======
        city = input("Please enter the name of a US city you would like to get weather info for: ")

        try:
            observation = owm.weather_at_place(city + ', US')
        except:
            print("You entered an invalid US city. Returning weather information for Boston...")
            observation = owm.weather_at_place('Boston, US')

        finally:
            w = observation.get_weather()

            # Set weather details
            weather.wind_speed = w.get_wind()['speed']             # returns dictionary with keys: 'speed', 'deg'
            weather.humidity = w.get_humidity()                    # 87
                    
            temperature = w.get_temperature('fahrenheit')       # returns a dictionary with keys: 'temp_max', 'temp', and 'temp_min'
            weather.temp_max = temperature['temp_max']
            weather.temp_current = temperature['temp']
            weather.temp_min = temperature['temp_min']
                    
            weather.status = w.get_status()
            weather.detailed_status = w.get_detailed_status()

            return weather

    except:
        print("Unable to authenticate session with provided credentials.")
        return None

# Uses simple conditionals to predict overall sentiment label
# given a weather object
def get_sentiment_label_weather(weather):
    if ( (weather.temp_current >= 75) and not( ('rain' in weather.status) or ('snow' in weather.status) or ('thunderstorm' in weather.status) ) ):
        label = 'positive'
    elif ( (weather.temp_current <= 50) and ( ('rain' in weather.status) or ('snow' in weather.status) or ('thunderstorm' in weather.status) ) ):
        label = 'negative'
    elif ( ( (weather.temp_current >= 75) and ( ('rain' in weather.status) or ('snow' in weather.status) or ('thunderstorm' in weather.status) ) ) or 
    ( (weather.temp_current <= 50) and ( ('clouds' in weather.status) or ('clear sky' in weather.status) ) ) ):
        label = 'mixed'
    else:
        label = 'neutral'

    return label

# Test code for above methods
if __name__ == '__main__':
    print('----- TEST FOR OWM MODULE ----- \n')

    print('*** Testing get_weather method ***')
    w = get_weather()
    print("Wind speed: ", w.wind_speed)
    print("Humidity: ", w.humidity)
    print("High (F): ", w.temp_max)
    print("Current temp (F): ", w.temp_current)
    print("Low (F): ", w.temp_min)
    print("Status (F): ", w.status)
    print("Detailed status (F): ", w.detailed_status)

    print('\n')
    print('*** Testing get_sentiment_label_weather method ***')
    # Test for positive
    w2 = weather(25, 0, 85, 76, 50, 'clouds', 'clouds')
    w2.display_weather()
    print( 'Sentiment label for inputted weather: ', get_sentiment_label_weather(w2) )

    # Test for negative
    w2 = weather(25, 0, 85, 45, 50, 'rain', 'clouds')
    w2.display_weather()
    print( 'Sentiment label for inputted weather: ', get_sentiment_label_weather(w2) )

    # Test for mixed
    w2 = weather(25, 0, 85, 80, 50, 'snow', 'clouds')
    w2.display_weather()
    print( 'Sentiment label for inputted weather: ', get_sentiment_label_weather(w2) )

    # Test for neutral
    w2 = weather(25, 0, 85, 60, 50, 'clouds', 'clouds')
    w2.display_weather()
    print( 'Sentiment label for inputted weather: ', get_sentiment_label_weather(w2) )

    print('\n')
    print('----- END TEST FOR OWM MODULE -----')
>>>>>>> tp-branch-1

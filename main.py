#Create a Mars Weather app using both the weather api & the rover image api

#imports
import requests, json
from config import api_key #api key is generated from creating a NASA account. It is stored within an .env file. The config file pulls it from the .env file.



#Weather data
response = requests.get("https://api.nasa.gov/insight_weather/?api_key={}&feedtype=json&ver=1.0".format(api_key))

res_stat_code = response.status_code
weather_data = response.json()
# print("weather data", weather_data['695'])

#Should really clean the below up and make it dynanmic. It is rather like messy like Derby County's season lol
for sol, values in weather_data.items():
    try:
        try:
            sol_details = {"sol": int(sol), "min_temp": values.get('AT', {}).get('mn'), "max_temp": values.get('AT', {}).get('mx')}

            if sol_details['min_temp'] == None:
                sol_details['min_temp'] = "n/a"

            print("Sol: {}, Min Temp: {}, Max Temp: {}".format(sol_details['sol'], sol_details['min_temp'], sol_details['max_temp']))
        except AttributeError:
            pass

    except ValueError:
        pass



#looking at images - some of them are pretty cool
response_img = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key={}".format(api_key))
image_data = response_img.json()
# print("image data", image_data)



# Per-Sol average values, linear sensors
# ● JSO[sol].AT.av - atmospheric temperature, degrees Celsius
# ● JSO[sol].PRE.av - atmospheric pressure, Pascals
# ● JSO[sol].HWS.av - horizontal wind speed, metres per second
# Per-sol 16-wind compass point of most common wind direction e.g. N for North or ESE for East-SouthEast
# ● JSO[sol].WD.most_common.compass_point

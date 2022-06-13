import requests
from weather.models import Forecast

def _get_forecast_json():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    encoded_city_name = 'Los%20Angeles'
    country_code = 'us'
    access_token = 'your_access_token'
  
    r = requests.get('{0}?q={1},{2}&APPID={3}'.format(
        url, 
        encoded_city_name, 
        country_code, 
        access_token))

    try:
        r.raise_for_status()
        return r.json()
    except:
        return None

      
def update_forecast():
    json = _get_forecast_json()
    if json is not None:
        try:
            new_forecast = Forecast()
            
            # open weather map gives temps in Kelvin. We want celsius.              
            temp_in_celsius = json['main']['temp'] - 273.15
            new_forecast.temperatue = temp_in_celsius
            new_forecast.description = json['weather'][0]['description']
            new_forecast.city = json['name']
            new_forecast.save()
            print("saving...\n" + new_forecast)
        except:
            pass
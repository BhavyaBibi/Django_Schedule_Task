import decimal
from datetime import datetime 
from django.shortcuts import render
from django.views.generic import TemplateView
from weather.models import Forecast
    

class MainPage(TemplateView):
    def get(self, request, **kwargs):
        
        latest_forecast = Forecast.objects.latest('timestamp')
        city = latest_forecast.city
        temperature_in_c = latest_forecast.temperatue
        temperature_in_f = (latest_forecast.temperatue * decimal.Decimal(1.8)) + 32
        description = latest_forecast.description.capitalize
        timestamp = "{t.year}/{t.month:02d}/{t.day:02d} - {t.hour:02d}:{t.minute:02d}:{t.second:02d}".format( t=latest_forecast.timestamp)


        return render(
            request, 
            'index.html', 
            {
                'city':city,
                'temperature_in_c': temperature_in_c,
                'temperature_in_f': round(temperature_in_f,2),
                'desctiprion': description,
                'utc_update_time': timestamp})
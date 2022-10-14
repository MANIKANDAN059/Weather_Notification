"""
	This the program to update weather using API
"""
import json
import requests
from pynotifier import Notification

def set_up():
    """
    Getting data from openweather api
    returns the required city data.
    """
    api_key="YOUR_API_KEY"
    city1="coimbatore"
    domain ="http://api.openweathermap.org"
    my_url="{}/data/2.5/weather?q={}&appid={}&units=metric".format(
		domain,
		city1,
		api_key
  				)
    response=requests.get(my_url)
    data=json.loads(response.text)
    return data

def notify(temp,humidity):
    """
    notify the temperature and humidity
    """
    Notification(
    title='weather Condition - Coimbatore',
    description={('Temp :',temp),('Humidity :',humidity)},
    duration=5,
    urgency='normal'
    ).send()

def get_data(info):
    """
    Getting the required city data.
    """
    temp=info["main"]["temp"]
    humidity=info["main"]["humidity"]
    notify(temp,humidity)
    print("climate is updated")
if __name__ == "__main__":
    get_data(set_up())

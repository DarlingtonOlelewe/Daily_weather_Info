import time
import requests

def sprint(string):
    print(string)
    time.sleep(1)


    

def city():
    sprint("\n Where in the world are You?")
    str = input()
    one = str.lower().split(" ")
    if len(one) > 1:
        return one[0]+"%20"+one[1]
    else: 
        return one[0]


def api(city_name):
    link = f'https://www.metaweather.com/api/location/search/?query={city_name}'
    city = requests.get(link)

    #  [{"title":"Lagos","location_type":"City","woeid":1398823,"latt_long":"6.439180,3.423480"}]

    woeid = str(city.json()[0]["woeid"])
    city_name = str(city.json()[0]["title"])

    second_link = f"https://www.metaweather.com/api/location/{woeid}/"

    about = requests.get(second_link)
    break_down = about.json()

    sprint(f"Weather for {city_name}")

    for daily in break_down["consolidated_weather"]:
        for value in daily:
            sprint(f"{value['applicable_date']}      {value['weather_state_name']}  High: {value['max_temp']}C  Low: {value['min_temp']}C")


def run():
    while True:
        city_name = city()
        api(city_name)


run()
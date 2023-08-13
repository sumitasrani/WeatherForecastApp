import requests

# Get lat & lon for place
def get_place(place):
    url_place = f"https://geocode.maps.co/search?city={place}"
    response = requests.get(url_place)
    info = response.json()
    lat = info[0]["lat"]
    lon = info[0]["lon"]
    return lat, lon

# Get Info: temp & weather, values for forecast days
def get_data(days, lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?" \
          f"latitude={lat}&longitude={lon}" \
          f"&hourly=temperature_2m,weathercode&forecast_days={days}"

    response = requests.get(url)
    info = response.json()
    value = 24 * days
    return info, value
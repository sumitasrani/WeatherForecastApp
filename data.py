import requests

def get_data(days, kind):
    url = f"https://api.open-meteo.com/v1/forecast?" \
          f"latitude=19.0728&longitude=72.8826" \
          f"&hourly=temperature_2m,weathercode&forecast_days={days}"

    response = requests.get(url)
    info = response.json()
    value = 24 * days
    time = info["hourly"]["time"][:value]
    print(info)
    print(value)
    print(time)
    if kind == "Temperature":
        temp = info["hourly"]["temperature_2m"][:value]

    if kind == "Weather":
        temp = info["hourly"]["weathercode"][:value]
    print(temp)
    print((len(temp)))
    return temp, time

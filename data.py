import requests

def get_data(days):
    url = f"https://api.open-meteo.com/v1/forecast?" \
          f"latitude=19.0728&longitude=72.8826" \
          f"&hourly=temperature_2m,weathercode&forecast_days={days}"

    response = requests.get(url)
    info = response.json()
    value = 24 * days
    return info, value

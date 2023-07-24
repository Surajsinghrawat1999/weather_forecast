import requests
API_KEY = "803a47834b9fad266400965ea41ec5aa"


def get_data(place, forecast_days=None, kind=None):


    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    nr_values = 8 * forecast_days
    filtered_data = data["list"]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))
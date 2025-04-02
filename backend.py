import requests

API_KEY = "141710af2113bab9f55ef73e1bcd33d5"

def get_data(place, forecast_days=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    content = response.json()
    filtered_data = content['list']
    nr_values = 8 * forecast_days
    return filtered_data[:nr_values]



if __name__ == '__main__':
    print(get_data(place='Tokyo', forecast_days=3))


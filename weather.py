import httpx

def get_weather(city: str):
    url = f'https://wttr.in/{city}?format=j1'
    response = httpx.get(url)
    return response.json()

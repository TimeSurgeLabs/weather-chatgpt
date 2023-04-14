from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

from weather import get_weather
from models import WeatherRequest

app = FastAPI(title="Weather API") # set title for ChatGPT
# required for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# test endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

# required for ChatGPT plugins to work
@app.get('/.well-known/ai-plugin.json', include_in_schema=False)
def read_ai_plugin_json() -> Response:
    with open('ai-plugin.json', 'r') as f:
        return Response(f.read(), media_type='application/json')

# get request example
@app.get('/weather/{city}', description="Get weather for a city.") # adding a description helps ChatGPT understand the endpoint
def get_weather_get(city: str):
    return get_weather(city)

# post request example
@app.post('/weather', description="Get weather for a city.")
def get_weather_post(request: WeatherRequest):
    return get_weather(request.city)

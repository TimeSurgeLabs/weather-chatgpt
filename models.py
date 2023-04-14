from pydantic import BaseModel

class WeatherRequest(BaseModel): # this model will be added to the OpenAPI schema
    city: str

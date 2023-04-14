FROM python:3.11-slim-buster

# link to the github repo
LABEL org.opencontainers.image.source=github.com/TimeSurgeLabs/weather-chatgpt

# install pipenv and update pip
RUN pip install --upgrade pipenv pip

WORKDIR /app

COPY . .

# install requirements to system
RUN pipenv install --system --deploy --ignore-pipfile

# run the app
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

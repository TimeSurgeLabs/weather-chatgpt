IMAGE_NAME := "ghcr.io/timesurgelabs/weather-chatgpt:main"

dev:
  uvicorn --reload --port 8000 --host 0.0.0.0 --reload main:app

build:
  docker build --platform linux/amd64 -t {{IMAGE_NAME}} .

run:
  docker run --platform linux/amd64 --rm -p 8000:8000 {{IMAGE_NAME}}

push:
  docker push {{IMAGE_NAME}}

# Weather ChatGPT Plugin Template

This repository contains a template for creating ChatGPT Plugins using FastAPI and OpenAPI. This specific template demonstrates how to build a plugin that interacts with a weather API to retrieve weather information for a specified city.

## What are ChatGPT Plugins?

ChatGPT Plugins are designed to connect OpenAI's ChatGPT to third-party applications, enhancing its capabilities and allowing it to interact with APIs defined by developers. With these plugins, ChatGPT can perform a wide range of actions such as:

* Retrieve real-time information (e.g., sports scores, stock prices, latest news)
* Access knowledge-base information (e.g., company docs, personal notes)
* Perform actions on behalf of the user (e.g., booking a flight, ordering food)

## Features

* FastAPI for API development
  + OpenAPI for API documentation is automatically generated, accelerating development
* Uvicorn for ASGI server
* Docker support
* Justfile for task automation

## Getting Started

1. Clone this repository.
2. Install dependencies using `pipenv install`.
3. Start the shell using `pipenv shell`.
4. Run the development server using the Justfile task: `just dev`.
5. Add your plugin to ChatGPT. See [here](https://platform.openai.com/docs/plugins/introduction/plugin-flow).

## Development

Make sure that you update `ai-plugin.json` with a detailed name and description for both ChatGPT and your potential users. You should also update the `Pipfile` with the correct dependencies for your plugin.

When you are developing your plugin, you can use the Justfile tasks to build and run your plugin. The `just dev` task will start the development server, which will automatically reload when you make changes to your code. The `just build` task will build a Docker image for your plugin. The `just run` task will run your plugin in a Docker container. Make sure you update the Justfile with the correct image name and tag.

## Files and Folders

* `Dockerfile`: Docker configuration file.
* `Justfile`: Justfile with tasks for development, building, and deploying.
* `Pipfile`: Pipenv configuration file for managing dependencies.
* `ai-plugin.json`: ChatGPT plugin configuration file.
* `main.py`: FastAPI application entry point.
* `models.py`: Pydantic models for API schema validation.
* `weather.py`: Module containing the function to fetch weather data.

## Deployment

When deploying, make sure you update the `ai-plugin.json` file with the correct URL for your plugin.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

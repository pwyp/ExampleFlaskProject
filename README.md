# ExampleFlaskProject

This is a simple [Flask](https://flask.palletsprojects.com/) application that provides two routes: a home route and a message analysis route.

__REMARK__: The vast majority of this project (directory structure, contents of files, unit tests, the skeleton of this README.md) was generated using the [GitHub Copilot](https://copilot.github.com/) and [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) plug-ins of [Visual Studio Code](https://code.visualstudio.com/).

## Prerequisities

* [curl](https://curl.se) (optional, just for testing purposes)
* [Python 3](https://www.python.org/)
* [pip](https://pip.pypa.io/)

## Installation

Create the environment:
```
> cd ExampleFlaskProject
> python -m venv .venv
> .venv\Scripts\activate.bat
```

Install the required packages using pip:
```
(env) pip install -r requirements.txt
```

## Running the Application
To run the application, navigate to the app directory and run the following command:
```
> cd ExampleFlaskProject
> python .\app\routes.py
```

## Usage
The application provides two routes:

1. Home route (```/```): Returns a JSON response with a 'message' key set to 'Hello, World!'.
    ```
    > curl -X GET http://localhost:5000
    ```
2. Message analysis route (```/analyze_message```): Analyzes the message received from the request and returns the word count.
    ```
    > curl -X POST -H "Content-Type: application/json" -d "{\"message\":\"Hello, World!\"}" http://localhost:5000/analyze_message
    ```


## Running Tests
To run tests, navigate to the tests directory and run the one of the following commands:
```
> cd ExampleFlaskProject
> python -m unittest discover -v
> python -m unittest -v .\tests\test_routes.py
```

## API Reference

### Get home
```
GET /
```
Returns a JSON response with a 'message' key set to 'Hello, World!'.

### Analyze message
```
POST /analyze_message
```
Analyzes the message received from the request and returns the word count.

| Parameter | Type | Description |
|-----------|------|-------------|
| ```message``` | ```string``` | __Required__. Your message |

## License
MIT
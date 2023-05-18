## OpenAI SDK Starter

The OpenAI SDK starter project with Python FastAPI is a comprehensive template that integrates OpenAI's language models into applications via a FastAPI-based web API. It includes OpenAPI documentation, enabling interactive documentation for API endpoints. Starlette Prometheus telemetry provides performance monitoring insights. Pytest unit testing ensures code reliability. The containerization example showcases packaging the application for easy deployment and scalability. This starter project offers a solid foundation for quickly building robust APIs that leverage OpenAI's language models, with documentation, monitoring, testing, and containerization capabilities.


## Set up the local development environment

Using a Python virtual environment allows multiple Python projects to run simultaneously on the same computer, with each project using different Python versions and different versions of third-party libraries without interfering with each other. This isolated environment ensures that the libraries used in one project will not conflict with those used in another project, thus avoiding errors caused by inconsistent versions or other factors. Virtual environments also make it easier for developers to share projects with others, as each person can create the same virtual environment on their own computer and install the same libraries, ensuring that the project has the same runtime environment on different computers.

Use the following command to create a Python virtual environment:


```bash
cd <project-home>
pyenv local 3.8.16
python -m venv venv
source venv/bin/activate
```


To run this starter application, you'll need to install FastAPI, the OpenAI SDK, and related packages in the requirements.txt file:

```
pip install -r requirements.txt

```

## Configuration

Environment variables are variables that are used to store configuration settings, API keys, or other sensitive information that should not be hard-coded into a project. `.env` allows developers to store these environment variables in a separate file, which can be loaded by the project at runtime.


| Variable   | Value Description |
|---------------|---------------------|
| OPENAI_API_KEY | The API key is used to authenticate and authorize API requests to the OpenAI platform |

## Run the application

```bash
uvicorn main:app --reload

```
or
```bash
python main.py
```

## Default Endpoints

| Endpoint          | Description                                                                                                   |
|---------------|-------------------------|
| http://localhost:8000 | Root API endpoint |
| http://localhost:8000/docs | The OpenAPI or Swagger API documentation and testing |
| http://localhost:8000/metrics | Prometheus monitoring metrics |



## Run Unit Test and Code Coverage

Pytest is a Python testing framework used for unit testing, functional testing, and integration testing of software applications.

Python coverage is a tool used to measure the code coverage of software applications written in Python. Code coverage refers to the percentage of code that is executed during a test run, and is a useful metric for evaluating the quality and completeness of test suites.

Use the following commands to run unit tests and code coverage:

```bash
coverage run -m pytest [--disable-warnings] -s
coverage report --show-missing
coverage html
```

To view the report, open the following URL:

> /htmlcov/index.html

## Running the application as a Docker container

Docker allows developers to package an application and its dependencies into a container that can be easily moved between environments, such as from a developer's laptop to a test environment or a production server. Containers are portable and self-contained, so they can be deployed quickly and reliably across different systems and environments, without worrying about dependencies or compatibility issues.

To create the Docker image:

```bash
docker build -t summarize:[<semantic version>] .

```

To run the built image as a container with the .env file:

```bash
docker run --rm -h localhost --env-file .env --name summarize -p 8000:8000 summarize:[<semantic version>]
```

## References

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI](https://platform.openai.com/docs/introduction)
- [FastAPI Prometheus Monitoring](https://github.com/trallnag/prometheus-fastapi-instrumentator)
- [PyTest - Unit testing](https://docs.pytest.org/en/7.1.x/contents.html)
- [Test Coverage](https://coverage.readthedocs.io/en/7.2.2/)

# API and UI Testing in Python - An introduction

## Install the Book Library Demo application

### Install the Frontend component:

1. Create a root folder for this project and open a terminal inside it
2. Clone [this repository](https://bitbucket.endava.com/projects/TDP/repos/pythonlibraryfrontend/browse).
3. `cd pythonlibraryfrontend`
4. Create a virtual environment and activate it

```
py -3 -m venv venv
./venv/Scripts/activate
```

5. Install the dependencies with `pip install -r requirements.txt`
6. Spin up the frontend component: `python front-end.py`

### Install the Backend component:

1. Change to the root directory and clone [this repository](https://bitbucket.endava.com/projects/TDP/repos/pythonlibrarybackend/browse).
2. `cd pythonlibrarybackend`
3. Create a virtual environment and activate it

```
py -3 -m venv venv
./venv/Scripts/activate
```

4. Install the dependencies with `pip install -r requirements.txt`
5. Spin up the backend component: `python back_end.py`
6. Verify app is runnig at (http://localhost:50001)[http://localhost:50001]

### Install the test suite

1. On the root directory:

```
git clone https://github.com/agustindangelo/python-testing.git
cd python-testing
```

## Executing tests

The [pytest library](https://docs.pytest.org/en/7.1.x/) is used as the test library for both API and E2E tests.

- To execute all tests: `pytest -v`
- To execute only API tests: `pytest -v ./api-tests/`
- To execute only E2E tests: `pytest -v ./e2e-tests/`
- To execute only the tests from a given file: `pytest -v ./api-tests/test_get_books.py`

## Generating interactive HTML reports with Allure

1. First of all, install Allure using **npm**: `npm install -g allure-commandline`
2. Now, run the tests specifying where the Allure report files should be saved: `pytest -v --alluredir=./reports/`
3. Serve the report files with `allure serve ./reports/`

## Useful documentation

- [Pytest - Python testing library](https://docs.pytest.org/en/7.1.x/)
- [Selenium with Python](https://selenium-python.readthedocs.io/)
- [Allure reporting for Pytest](https://docs.qameta.io/allure/#_pytest)

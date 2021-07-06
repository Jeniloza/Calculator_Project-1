FROM python:3

ADD src /src

run pip install coverage

CMD [ "python", "./src/CalculatorTests.py" ]
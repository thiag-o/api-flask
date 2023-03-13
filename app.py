from flask import Flask
from flask import request

app = Flask(__name__)


def soma(numbers):
    soma = 0
    for i in range(0, len(numbers)):
        soma += numbers[i]
    return soma

@app.route("/")
def hello_world():
    return "Hello, World"


@app.post('/soma')
def post_soma():
    content = request.json;
    arrayNumbers = content['numbers']
    return f"soma é {soma(arrayNumbers)}"

@app.post('/subtracao')
def post_subtracao():
    content = request.json;
    numbers = content['numbers']
    return f"subtracao é {numbers[0] - numbers[1]  }"


@app.post('/multiplicacao')
def post_multiplicacao():
    content = request.json;
    numbers = content['numbers']
    return f"multiplicacao é {numbers[0] * numbers[1] }"


@app.post('/divisao')
def post_divisao():
    content = request.json;
    numbers = content['numbers']
    return f"divisao é {numbers[0] / numbers[1] }"


@app.post('/potencia')
def post_potencia():
    content = request.json;
    numbers = content['numbers']
    return f"potencia é {numbers[0] ** numbers[1] }"
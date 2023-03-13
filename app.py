from flask import Flask
from flask import request
import math
import statistics

#$ flask --app app run --debug
app = Flask(__name__)


def soma(numbers):
    soma = 0
    for i in range(0, len(numbers)):
        soma += numbers[i]
    return soma

def mediaAritimetica(numbers):
   somaAritimetica =  soma(numbers)
   return somaAritimetica/len(numbers)

def mediaHarmonica(numbers):
    somaHarmonica = 0
    for i in range(0, len(numbers)):
        somaHarmonica += 1/numbers[i]
    return len(numbers)/somaHarmonica

    

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
    return f"subtracao é {numbers[0] - numbers[1] }"


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


@app.post('/raiz-quadrada')
def post_raiz_quadrada():
    content = request.json;
    number = content['number']
    return f"raiz quadrada de {number} é {math.sqrt(number) }"



@app.post('/media-aritimetica')
def post_media_aritimetica():
    content = request.json;
    numbers = content['numbers']
    return f"a media aritimética é {mediaAritimetica(numbers) }"

@app.post('/media-harmonica')
def post_media_harmonica():
    content = request.json;
    numbers = content['numbers']
    return f"a media harmonica é {mediaHarmonica(numbers) }"
@app.post('/moda')
def post_moda():
    content = request.json;
    numbers = content['numbers']
    return f"a moda é {statistics.mode(numbers) }"

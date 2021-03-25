from flask import Flask
from calculadora import Calculadora

app = Flask(_name_)

@app.route('/')
def hola():
    return 'Hola mundo'

@app.route('/suma/<int:valor_1>/<int:valor_2>')
def suma(valor_1, valor_2):
    c = Calculadora()
    c.valor_1 = valor_1
    c.valor_2 = valor_2
    c.sumar()
    return (str(c.valor_1)+" + "+ str(c.valor_2)+"="+ str(c.resultado))

@app.route('/resta/<int:valor_1>/<int:valor_2>')
def resta(valor_1, valor_2):
    c = Calculadora()
    c.valor_1 = valor_1
    c.valor_2 = valor_2
    c.restar()
    return (str(c.valor_1)+" - "+ str(c.valor_2)+"="+ str(c.resultado))

@app.route('/multiplicacion/<int:valor_1>/<int:valor_2>')
def multiplicacion(valor_1, valor_2):
    c = Calculadora()
    c.valor_1 = valor_1
    c.valor_2 = valor_2
    c.multiplicar()
    return (str(c.valor_1)+" * "+ str(c.valor_2)+"="+ str(c.resultado))

@app.route('/divicion/<int:valor_1>/<int:valor_2>')
def divicion(valor_1, valor_2):
    c = Calculadora()
    c.valor_1 = valor_1
    c.valor_2 = valor_2
    c.dividir()
    return (str(c.valor_1)+" / "+ str(c.valor_2)+"="+ str(c.resultado))

@app.route('/operacion/<operador>/<int:valor_1>/<int_valor_2>')
def operacion(operador, valor_1, valor_2):
    if operador == "+":
        return suma(valor_1, valor_2)
    elif operador == "-"
        return resta(valor_1, valor_2)
    elif operador == "*"
        return multiplicacion(valor_1, valor_2)
    elif operador == "/"
        return divicion(valor_1, valor_2)
    else:
        return hola()

if __name__ == '_main_':
    app.run(debug =  True)
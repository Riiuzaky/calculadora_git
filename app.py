from flask import Flask
from calculadora import Calculadora

app = Flask(_name_)

@app.route('/')
def hola():
    return 'Hola mundo'

if __name__ == '_main_':
    app.run(debug =  True)
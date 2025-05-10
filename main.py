from flask import Flask # Importando classe Flask do Módulo flask

app = Flask(__name__) # Criando uma instância da classe Flask

@app.route("/") # Decorador que define a rota da aplicação
def hello_world():# Define a função hello_world que será chamada quando a rota for acessada
    return "<p>Hello World!</p>"

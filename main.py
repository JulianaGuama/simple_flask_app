from flask import Flask

# Instanciando a classe base do Flask
app = Flask(__name__) #->

# criação da rota
@app.route('/')
def main():
    return "Hello World!"

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '3000'))
    except ValueError:
        PORT = 3000
    app.run(HOST, PORT)
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH"

@app.route('/saluda')
def saludar():
    return "habia una vez, un barquito que no sabia navegar..."

@app.route('/suma')
def suma():
    a = request.args.get('a')
    b = request.args.get('b')
    resultado =  a + b
    return "la suma es " + resultado

if __name__ == "__main__":
    app.run()
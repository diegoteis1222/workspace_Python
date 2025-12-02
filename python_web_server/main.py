from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

@app.route('/')
def home():
    return "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH"

@app.route('/saluda')
def saludar():
    return "habia una vez, un barquito que no sabia navegar..."

@app.route('/suma')
def suma():
    a = request.args.get('a', type=int, default=0)
    b = request.args.get('b', type=int, default=0)
    resultado =  a + b
    return f"La suma de {a} + {b} es: {resultado}"

form_html = '''
<form method="POST" action="/login">
    Usuario: <input type="text" name="usuario"><br>
    Contraseña: <input type="password" name="password"><br>
    <input type="submit" value="Login">
</form>
'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template_string(form_html)
    elif request.method == 'POST':
        usuario = request.form.get('usuario', default='')
        password = request.form.get('password', default='')
        if usuario == 'root' and password == '1234':
            return "Login exitoso", 200
        else:
            return "Usuario o contraseña incorrectos", 401
    else:
        pass
    
@app.route('/api/suma' , methods=['POST'])
def api_suma():
    data = request.get_json()
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    resultado =  num1 + num2
    diccionario = {"resultado": resultado}
    return jsonify(diccionario)

if __name__ == "__main__":
    app.run()
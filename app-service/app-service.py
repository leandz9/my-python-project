from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Bem-vindo à aplicação Flask!"

@app.route('/health')
def health_check():
    return jsonify(status="ok")
@app.route('/rota1')
def rota1():
    return jsonify(status="ok")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
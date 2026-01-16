from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template('home.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/salvar')
def salvar():
    return 'salvo com sucesso'

app.run(debug=True)
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
  retorno = 'A API está online.</br>'
  retorno += '<h3>Métodos da API</h3>'
  retorno += '<em>/somar/v1/v2</em> - Retorna a soma entre dois valores v1 e v2</br>'
  retorno += '<em>/multiplicar/v1/v2</em> - Retorna a multiplicação entre dois valores v1 e v2</br>'
  retorno += '<em>/previa</em> - Retorna os cinco primeiros registros de um <em>dataset</em> sobre vendas</br>' 
  retorno += '<em>/totalvendas</em> - Retorna o total das vendas de um <em>dataset</em> sobre vendas</br>'
  return retorno
  

@app.route('/somar/<string:v1>/<string:v2>')
def somar(v1, v2):
  retorno = {'operacao':'adição', 'v1':v1, 'v2':v2,'resultado':int(v1)+int(v2)}
  return jsonify(retorno)

@app.route('/multiplicar/<string:v1>/<string:v2>')
def multiplicar(v1, v2):
  retorno = {'operacao':'multiplicação', 'v1':v1, 'v2':v2,'resultado':int(v1)*int(v2)}
  return jsonify(retorno)

@app.route('/previa') 
def previa():
  dados = pd.read_csv('https://github.com/rodrigonerisalves/desafio-api-flask/blob/main/vendas.csv')
  resposta = dados.head(5).to_dict(orient="list")
  return jsonify(resposta)
  
@app.route('/totalvendas')
def vendas():
  dados = pd.read_csv('https://github.com/rodrigonerisalves/desafio-api-flask/blob/main/vendas.csv')
  resposta = {'total_vendas':dados.Vendas.sum()}
  return jsonify(resposta)
  
app.run('0.0.0.0', debug=True)

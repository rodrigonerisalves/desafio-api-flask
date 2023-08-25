**O desafio de projeto tem como objetivo apresentar o desenvolvimento de uma API simples que utiliza Python/Flask**

# 🔧 Apresentação do código

Vou dividir o código em partes e explicar cada uma delas:

**Parte 1: Importação de bibliotecas**
```python
import pandas as pd
from flask import Flask, jsonify
```
Nessa parte, estamos importando as bibliotecas necessárias para o código. O `pandas` é usado para manipulação de dados e o `Flask` é um framework web em Python que permite construir APIs.

**Parte 2: Criação do objeto Flask**
```python
app = Flask(__name__)
```
Aqui, estamos criando um objeto Flask, que é a base da nossa aplicação web.

**Parte 3: Rota para a página inicial**
```python
@app.route('/')
def homepage():
  retorno = 'A API está online.</br>'
  retorno += '<h3>Métodos da API</h3>'
  retorno += '<em>/somar/v1/v2</em> - Retorna a soma entre dois valores v1 e v2</br>'
  retorno += '<em>/multiplicar/v1/v2</em> - Retorna a multiplicação entre dois valores v1 e v2</br>'
  retorno += '<em>/previa</em> - Retorna os cinco primeiros registros de um <em>dataset</em> sobre vendas</br>' 
  retorno += '<em>/totalvendas</em> - Retorna o total das vendas de um <em>dataset</em> sobre vendas</br>'
  return retorno
```
Aqui, definimos a rota inicial ("/") da nossa API. Quando essa rota é acessada, a função `homepage()` é chamada. Essa função retorna uma string HTML com informações sobre os métodos disponíveis na API.

**Parte 4: Rota para soma**
```python
@app.route('/somar/<string:v1>/<string:v2>')
def somar(v1, v2):
  retorno = {'operacao':'adição', 'v1':v1, 'v2':v2,'resultado':int(v1)+int(v2)}
  return jsonify(retorno)
```
Nesta parte, definimos a rota "/somar" da nossa API. Ela recebe dois parâmetros (`v1` e `v2`) na URL e retorna a soma desses dois valores. O resultado é retornado em formato JSON.

**Parte 5: Rota para multiplicação**
```python
@app.route('/multiplicar/<string:v1>/<string:v2>')
def multiplicar(v1, v2):
  retorno = {'operacao':'multiplicação', 'v1':v1, 'v2':v2,'resultado':int(v1)*int(v2)}
  return jsonify(retorno)
```
Nesta parte, definimos a rota "/multiplicar" da nossa API. Ela também recebe dois parâmetros (`v1` e `v2`) na URL e retorna a multiplicação desses dois valores. O resultado é retornado em formato JSON.

**Parte 6: Rota para visualização dos primeiros registros**
```python
@app.route('/previa') 
def previa():
  dados = pd.read_csv('https://github.com/rodrigonerisalves/desafio-api-flask/blob/main/vendas.csv')
  resposta = dados.head(5).to_dict(orient="list")
  return jsonify(resposta)
```
Aqui, definimos a rota "/previa" da nossa API. Quando essa rota é acessada, a função `previa()` é chamada. Essa função lê um arquivo CSV de vendas a partir de uma URL e retorna os cinco primeiros registros desse conjunto de dados em formato JSON.

**Parte 7: Rota para retorno do total de vendas**
```python
@app.route('/totalvendas')
def vendas():
  dados = pd.read_csv('https://github.com/rodrigonerisalves/desafio-api-flask/blob/main/vendas.csv')
  resposta = {'total_vendas':dados.Vendas.sum()}
  return jsonify(resposta)
```
Nesta parte, definimos a rota "/totalvendas" da nossa API. Ao ser acessada, a função `vendas()` é chamada. Essa função lê um arquivo CSV de vendas a partir de uma URL e retorna o total das vendas desse conjunto de dados em formato JSON.

**Parte 8: Inicialização da API**
```python
app.run('0.0.0.0', debug=True)
```
Por fim, estamos iniciando a API chamando a função `run()` do objeto Flask. O parâmetro `'0.0.0.0'` indica que a API estará disponível em todas as interfaces de rede. O parâmetro `debug=True` habilita o modo de depuração, o que é útil durante o desenvolvimento.

## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [Visual Studio Code](https://code.visualstudio.com/) - Code Editing


## ✒️ Autores


* **Rodrigo Neris** -  [*Trabalho Inicial*](https://github.com/rodrigonerisalves)
---
⌨️ com ❤️ por [Rodrigo Neris](www.linkedin.com/in/rodrigo-neris) 😊
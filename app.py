from flask import flash, Flask, render_template, redirect, request
import requests


app = Flask(__name__)

ENDPOINT_API = "https://api.thecatapi.com/v1/images/search"
app.secret_key = 'sla'

#Rota da página inicial
@app.route('/', methods = ['GET'])
def index():
    return render_template("index.html")


#Rota para processar a solicitação
@app.route('/cat', methods = ['GET','POST'])
def cat():
    if request.method == 'GET':
        return redirect('/')
    
    name = request.form.get('name', None)
    
    if not name:
        flash("ERRO, insira um nome")
        return redirect('/')
    
    answer = requests.get(ENDPOINT_API) #Consultando
    if answer.status_code == 200:
        data = answer.json()#Tranformando em dicionário
        url_image = data[0]['url']
    else:
        flash("ERRO! infelizmente você não é um gatinho")
        return redirect('/')
    
    return render_template('index.html',
                           url_image = url_image,
                           name = name)









if __name__ == "__main__":
    app.run(debug = True)
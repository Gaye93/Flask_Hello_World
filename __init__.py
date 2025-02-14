from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>" #comm

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route("/contact/")
def MaPremiereAPI():
    return render_template('contact.html')
  
@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)
  
@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    total = valeur1 + valeur2
    if total % 2 == 0:
        resultat = "pair"
    else:
        resultat = "impair"
    
    return f"<h2>La somme de vos valeurs est : {total}</h2><p>Ce nombre est {resultat}.</p>"

@app.route('/sommes/<path:valeurs>')
def sommes(valeurs):
    # Séparer les valeurs par des barres obliques et les convertir en une liste d'entiers
    nombres = list(map(int, valeurs.split('/')))
    # Calculer la somme des nombres
    total = sum(nombres)
    # Afficher la somme
    return f"<h2>La somme de vos valeurs est : {total}</h2>"
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)


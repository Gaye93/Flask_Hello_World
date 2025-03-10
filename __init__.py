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

@app.route("/exercice_base1/")
def exo1():
    return render_template('1_Liste_Base.html')

@app.route("/exercice_base2/")
def exo2():
    return render_template('exercice2.html')

@app.route("/exercice_base3/")
def exo3():
    return render_template('exercice3.html')

@app.route("/TP1/")
def tp():
    return render_template('TP1.html')

@app.route("/formulaire/")
def form():
    return render_template('formulaire.html')

@app.route("/exemple_base/")
def exempleSVG():
    return render_template('Exemple_Base_SVG.html')

@app.route("/maison/")
def maisonSVG():
    return render_template('exercice_1_SVG.html')

@app.route("/vallet/")
def valletSVG():
    return render_template('exercice_2_SVG.html')

@app.route("/etoiles/")
def etoiles():
    return render_template('Carre_Etoiles.html')

@app.route("/chenille/")
def chenilleSVG():
    return render_template('exercice_3_SVG.html')

@app.route("/carre/")
def carreCSS():
    return render_template('CSS_Carre.html')

@app.route("/cnam/")
def cnam():
    return render_template('cnam.html')
  
@app.route("/cv/")
def monCV():
    return render_template('cv.html')
  
  
@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)

@app.route('/calcul_somme/<int:valeur1>/<int:valeur2>')
def calcul_somme(valeur1, valeur2):
    total = valeur1 + valeur2
    return f"<h2>La somme de vos valeurs est: {total}</h2>"

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
  
@app.route('/max/<path:valeurs>')
def valeur_maximale(valeurs):
    # Séparer les valeurs par des barres obliques et les convertir en une liste d'entiers
    nombres = list(map(int, valeurs.split('/')))
    # Trouver la valeur maximale en utilisant une boucle
    max_valeur = nombres[0]  # Initialiser la première valeur comme maximale
    for nombre in nombres:
        if nombre > max_valeur:
            max_valeur = nombre  # Si on trouve une valeur plus grande, on la met à jour
    # Afficher la valeur maximale
    return f"<h2>La valeur la plus importante est : {max_valeur}</h2>"
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)


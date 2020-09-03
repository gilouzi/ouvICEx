import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, Blueprint, render_template, request, send_file
from scripts.database import posts, db

app_analyses = Blueprint("app_analyses", __name__, template_folder="templates")
@app_analyses.route("/analyses", methods=["POST", "GET"])
def analyses():
	
	# simulação da leitura de dados do banco
	X = np.random.randn(30)
	Y = 2 * X
	
	
	if request.method == "GET": # se estiver apenas carregando a página
		return render_template(
			"analyses.html",
	 		values = posts.query.all()
		)
	elif request.method == "POST": # senão, se for o caso de requisição
		grafico = "/static/graficos/" # folder base das imagens
		btn = str(request.form["btn_plot"]) # avalia qual botão foi clicado
		if btn == "Exibir scatter": # se for o de scatter
			figura = plt.scatter(X, Y) # produz o gráfico
			grafico += "scatter1.png" # aponta pro local onde será salvo
		elif btn == "Exibir histograma": # faz a mesma avaliação para todos botões possíveis
			figura = plt.hist(X)
			grafico += "hist1.png"
		
		plt.savefig("ouvICEx" + grafico) # salva o gráfico
		plt.close()
		
		return render_template( 
			"analyses.html",
	 		values = posts.query.all(),
	 		grafico = grafico
		)
		

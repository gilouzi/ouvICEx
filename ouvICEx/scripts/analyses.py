import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, Blueprint, render_template, request, send_file
from scripts.database import posts, db

app_analyses = Blueprint("app_analyses", __name__, template_folder="templates")

def get_posts_df():
	values = posts.query.all()
	return type(values[0])

def get_statistics(values, est, filtro):
	labels = ['a', 'b']
	totals = [5, 12]
	
	return labels, totals

@app_analyses.route("/analyses", methods=["POST", "GET"])
def analyses():
	map_value_output = {
		'real': 'Total de denúncias realizadas',
		'apur': 'Total de denúncias apuradas',
		'per': 'Período',
		'depto': 'Departamento',
		'cont': 'Contexto',
		'tipo': 'Tipo'
	}
	
	# simulação da leitura de dados do banco
	X = np.random.randn(30)
	Y = 2 * X
	
	if request.method == "GET": # se estiver apenas carregando a página
		grafico = "/static/graficos/empty.png"
		titulo = ""
		figura = plt.scatter([], []) # produz o gráfico
		plt.savefig("ouvICEx" + grafico) # salva o gráfico
		plt.close()
		
		return render_template(
			"analyses.html",
	 		values = posts.query.all(),
			grafico = grafico,
	 		titulo = titulo
		)
	elif request.method == "POST": # senão, se for o caso de requisição
		grafico = "/static/graficos/" # folder base das imagens
		est = str(request.form["est"]) # avalia qual estatística foi selecionada
		filt = str(request.form["filtro"]) # avalia qual filtro foi selecionado
		est = map_value_output[est]
		filt = map_value_output[filt]
		titulo = est + ' por ' + filt
		
		labels, totals = get_statistics(posts.query.all(), est, filt)
		
		#btn = str(request.form["btn_plot"]) # avalia qual botão foi clicado		
		#if btn == "Exibir scatter": # se for o de scatter
		#	figura = plt.scatter(X, Y) # produz o gráfico
		#	grafico += "scatter1.png" # aponta pro local onde será salvo
		#elif btn == "Exibir histograma": # faz a mesma avaliação para todos botões possíveis
		#	
		#	grafico += "hist1.png"
			
		grafico += est + filt + ".png"
		figura = plt.bar(labels, totals)
		
		#plt.title(titulo)
		plt.savefig("ouvICEx" + grafico) # salva o gráfico
		plt.close()
		
		return render_template( 
			"analyses.html",
	 		values = posts.query.all(),
	 		grafico = grafico,
	 		titulo = titulo
		)
		

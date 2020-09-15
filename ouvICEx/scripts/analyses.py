import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, Blueprint, render_template, request, send_file
from scripts.database import posts, db

app_analyses = Blueprint("app_analyses", __name__, template_folder="templates")

def get_statistics(values, est, filtro):
	categories = ['ref_dep', 'author_dep', 'context_t', 'situation_t', 'date']
	dict_totals = {cat:{} for cat in categories}
	for vl in values:
		if vl.ref_dep not in dict_totals['ref_dep'].keys(): # ref_dep
			dict_totals['ref_dep'][vl.ref_dep] = 0
		else:
			dict_totals['ref_dep'][vl.ref_dep] += 1
			
		if vl.author_dep not in dict_totals['author_dep'].keys(): # author_dep
			dict_totals['author_dep'][vl.author_dep] = 0
		else:
			dict_totals['author_dep'][vl.author_dep] += 1
			
		if vl.context_t not in dict_totals['context_t'].keys(): # context_t
			dict_totals['context_t'][vl.context_t] = 0
		else:
			dict_totals['context_t'][vl.context_t] += 1		
			
		if vl.situation_t not in dict_totals['situation_t'].keys(): # situation_t
			dict_totals['situation_t'][vl.situation_t] = 0
		else:
			dict_totals['situation_t'][vl.situation_t] += 1		
			
		if str(vl.date) not in dict_totals['date'].keys(): # date
			dict_totals['date'][str(vl.date)] = 0
		else:
			dict_totals['date'][str(vl.date)] += 1				
	
	labels = list(dict_totals[filtro].keys())
	totals = list(dict_totals[filtro].values())
	
	return labels, totals, dict_totals

@app_analyses.route("/analyses", methods=["POST", "GET"])
def analyses():
	map_value_output = {
		'real': 'Total de denúncias realizadas',
		'apur': 'Total de denúncias apuradas',
		'date': 'Período',
		'ref_dep': 'Departamento',
		'context_t': 'Contexto',
		'situation_t': 'Tipo'
	}
	
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
		
		labels, totals, dict_totals = get_statistics(posts.query.all(), est, filt)
			
		est = map_value_output[est]
		filt = map_value_output[filt]
		titulo = est + ' por ' + filt
		est = est.replace(' ', '_')
		filt = filt.replace(' ', '_')
		grafico += est + filt + ".png"
		figura = plt.bar(labels, totals)
		plt.xticks(rotation = 15)
		
		plt.savefig("ouvICEx" + grafico) # salva o gráfico
		plt.close()
		
		return render_template( 
			"analyses.html",
	 		values = posts.query.all(),
	 		grafico = grafico,
	 		titulo = titulo,
	 		dict_totals = labels
		)
		

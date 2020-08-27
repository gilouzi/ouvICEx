import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, Blueprint, render_template, request, flash
from scripts.database import posts, db

app_analyses = Blueprint("app_analyses", __name__, template_folder="templates")
@app_analyses.route("/analyses", methods=["POST", "GET"])
def analyses():
	
	X = np.random.randn(30)
	Y = 2 * X
	
	if request.method == "GET":
		return render_template(
			"analyses.html",
	 		values = posts.query.all()
		)
	elif request.method == "POST":
		btn = str(request.form["btn_plot"])
		
		if btn == "Exibir scatter":
			grafico = "nesse caso viria um scatter"
			figura = plt.scatter(X, Y)
		elif btn == "Exibir histograma":
			grafico = "nesse caso viria um histograma"
			figura = plt.hist(X)
			
		plt.savefig("grafico.png")
		
		return render_template(
			"analyses.html",
	 		values = posts.query.all(),
	 		grafico = grafico,
	 		PNG = "grafico.png"
		)
		

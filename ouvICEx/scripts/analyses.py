import pandas as pd
from flask import Flask, Blueprint, render_template, request, flash
from scripts.database import posts, db

app_analyses = Blueprint("app_analyses", __name__, template_folder="templates")
@app_analyses.route("/analyses", methods=["POST", "GET"])
def analyses():
	teste = values = posts.query.all()
	if request.method == "GET":
		return render_template(
			"analyses.html",
	 		values = posts.query.all()
		)
	elif request.method == "POST":
		btn = str(request.form["btn_plot"])
		
		if btn == "Exibir scatter":
			grafico = "nesse caso viria um scatter"
		elif  btn == "Exibir barplot":
			grafico = "nesse caso viria um barplot"
			
		return render_template(
			"analyses.html",
	 		values = posts.query.all(),
	 		grafico = grafico
		)
		

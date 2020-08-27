import pandas as pd
from flask import Flask, Blueprint, render_template, request, flash
from scripts.database import posts, db

app_analyses = Blueprint("app_analyses", __name__, template_folder="templates")
@app_analyses.route("/analyses", methods=["POST", "GET"])
def analyses():
	if request.method == "GET":
		return render_template(
			"analyses.html",
	 		values = posts.query.all()
		)
	elif request.method == "POST":
		btn = request.form["btn_plot"]
		return str(btn)
		#return render_template(
		#	"form.html",
	 	#	values = posts.query.all()
		#)

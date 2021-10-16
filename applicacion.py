from flask import Flask, render_template, request, Response, redirect, url_for

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("login.html")
"""@app.route('/curriculum/')
def curriculum():
	return render_template("formulario.html")"""
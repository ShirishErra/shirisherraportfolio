from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/shirishportfolio')
def home():
    return render_template('portfolio.html')

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello Kori!"
	
@app.route("/news")
def news():
	return "news"
	
@app.route("/Submit")
def submission():
	return "submit"
	
@app.route("/contactUs")
def contact():
	return "Karan Erry"
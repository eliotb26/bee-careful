from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template('homescreen.html')
	
@app.route("/news")
def news():
	return "news"
	
@app.route("/Submit")
def submission():
	return "submit"
	
@app.route("/contactUs")
def contact():
	return "Karan Erry"


if __name__ == '__main__':
	app.run(debug=True)
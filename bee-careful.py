from flask import Flask, render_template
app = Flask(__name__, static_folder='static', static_url_path='/static')
#app.static_folder = "/static"

@app.route("/")
@app.route("/home")
def home():
	return render_template('templates2.html')
	
@app.route("/news")
def news():
	return "news"
	
@app.route("/Submit")
def submission():
	return "submit"
	
@app.route("/contactUs")
def contact():
	return "Karan Erry"

@app.route("/profile")
def profile():
	return "Test"

if __name__ == '__main__':
	app.run(debug=True)
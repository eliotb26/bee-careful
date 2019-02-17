from flask import Flask, render_template, request
from xml.dom import minidom
import xml.etree.ElementTree as ET
app = Flask(__name__, static_folder='static')

@app.route("/")
@app.route("/home")
def home():
	return render_template('templates2.html')
	
@app.route("/news")
def news():
	return render_template('news.html')
	
@app.route("/submit", methods=['GET', 'POST'])
def submit():
	if request.method == 'POST' and all(elem in request.form for elem in ['user', 'site', 'fields', 'uses']):
		if validate_user(request.form['user']):
			return update_site_data(request.form['site'], request.form['fields'], request.form['uses'])
	return render_template('submit.html', inputError = True)
	
@app.route("/contact-us")
def contact():
	return "Karan"

@app.route("/profile")
def profile():
	return "Test"
	
##############################
# 	  INTERNAL FUNCTIONS	 #
##############################

def update_site_data(address, fields, uses):
	# parse fields and uses
	# then store in db for address
	# catches exception which returns submit with error=True
	# otherwise returns void
	pass

def validate_user(username):
	# check db and validate
	# returns boolean
	pass
		
##############################
# 	  		 XML			 #
##############################

def initializeDataObjects():
	global root, elem_sites, elem_fields, elem_users
	try:
		root = ET.parse('database.xml').getroot()
		elem_sites, elem_fields, elem_users = root.find('sites'), root.find('fields'), root.find('users')
	except FileNotFoundError:
		print('database.xml file could not be found. Creating new file in current dir.')
		root = ET.Element('data')
		elem_sites, elem_fields, elem_users = ET.SubElement(root, 'sites'), ET.SubElement(root, 'fields'), ET.SubElement(root, 'users')
		ET.SubElement(elem_trips, 'count').text = '0'


if __name__ == '__main__':
	app.run(debug=True)

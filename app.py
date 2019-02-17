from flask import Flask, render_template, request, redirect, url_for
from xml.dom import minidom
import xml.etree.ElementTree as ET
app = Flask(__name__, static_folder='static')

@app.route("/")
@app.route("/home")
def home():
	return render_template('home-screen.html')
	
@app.route("/news")
def news():
	return render_template('news.html')
	
@app.route("/submit", methods=['GET', 'POST'])
def submit():
	# TODO remove debug statements
#	print('--- A ---')
#	initializeDataObjects()
#	print('--- AA ---')
#	if request.method == 'POST':
#		print('--- B ---')
	errMsg = ''
	if request.method == 'POST' and all(elem in request.form for elem in ['user', 'site', 'fieldusages']):
		print('--- 0 ---')
		if validate_user(request.form['user']):
			status = add_site_data(request.form['site'], request.form['fieldusages'])
			if status == 'GREEN':
				tree = ET.ElementTree(root)
				tree.write('database.xml')
				tree.write('database_backup.xml')
				print(minidom.parse('database.xml').toprettyxml())
				return redirect(url_for('home'))
			else:	errMsg = 'problems parsing data. did you follow all the instructions closely?'
		else:	errMsg = 'your user does not seem to exist. click "add user" to add yourself!'
	elif request.method == 'POST':
		errMsg = 'did you enter values for each field?'
	return render_template('submit.html', errMsg = errMsg)
	
@app.route("/contact-us")
def contact():
	return render_template('Context_us.html')

@app.route("/profile")
def profile():
	return "Test"
	
@app.route("/add-contributor")
	
##############################
# 	  INTERNAL FUNCTIONS	 #
##############################

def update_site_data(site, fields, uses):
	# parse fields and uses
	# then store in db for address
	# catches exception which returns submit with error=True
	# otherwise returns void
	pass

def validate_user(username):
	# check db and validate
	# returns boolean
	# TODO: VALIDATE THE USER FOR REAL !!!
	return True
		
##############################
# 	  	  DATA  BASE	 	 #
##############################

global root, elem_sites, elem_fields, elem_usages, elem_users

def initializeDataObjects():
	global root, elem_sites, elem_fields, elem_usages, elem_users
	try:
		root = ET.parse('database.xml').getroot()
		elem_sites, elem_fields, elem_users = root.find('sites'), root.find('fields'), root.find('users')
	except FileNotFoundError:
		print('database.xml file could not be found. Creating new file in current dir.')
		root = ET.Element('data')
		elem_sites, elem_fields, elem_usages, elem_users = ET.SubElement(root, 'sites'), ET.SubElement(root, 'fields'), ET.SubElement(root, 'usages'), ET.SubElement(root, 'users')

# def addField(fieldToAdd): # done, untested
# 	for field in elem_fields.findall('field'):
# 		if field.text == fieldToAdd:
# 			return True
# 	newField = ET.SubElement(elem_fields, 'field')
# 	newField.text = fieldToAdd
# 	return True
#
#
# def addUsage(usageToAdd): # done, untested
# 	for usage in elem_usages.findall('usage'):
# 		if usage.text == usageToAdd:
# 			return True
# 	newUsage = ET.SubElement(elem_usages, 'usage')
# 	newUsage.text = usageToAdd
# 	return True

def getFieldForSite(fieldName, site):	# done, untested
	# site = elem_sites.find('site', {'addr':siteAddr})
	for field in site.findall('field'):
		if field.attrib['name'] == fieldName:
			return field
	# Program flow reached here so no field found
	# Create field
	newField = ET.SubElement(site, 'field', {'name':fieldName})
	return newField

def getUsageForField(usageName, field):	# done, untested
	for usage in field.findall('usage'):
		if usage.text == usageName:
			usage.attrib['count'] = str(int(usage.attrib['count']) + 1)
			return usage
	# Program flow reached here so no usage found
	# Create usage
	newUsage = ET.SubElement(field, 'usage', {'count':'1'})
	newUsage.text = usageName
	return newUsage


# def getField(fieldName):	# done, untested
# 	for field in elem_fields.findall('field'):
# 		if field.text == fieldName:
# 			return field
# 	# Program flow reached here so no field found
# 	# Create field
# 	newField = ET.SubElement(elem_fields, 'field')
# 	newField.text = fieldName
# 	return newField
#
# def getUsage(usageName):	# done, untested
# 	for usage in elem_usages.findall('usage'):
# 		if usage.text == usageName:
# 			return usage
# 	# Program flow reached here so no usage found
# 	# Create usage
# 	newUsage = ET.SubElement(elem_usages, 'usage')
# 	newUsage.text = usageName
# 	return newUsage


def add_site_data(addr, field_usage):
	try:
		field_usage_pairs = [value.strip() for value in field_usage.split(';')]
		# get site
		site = getSite(addr)
		for pair in field_usage_pairs:
			fieldName, usages = [value.strip() for value in pair.split(':')]
			usageNames = [value.strip() for value in usages.split(',')]
			# get field
			field = getFieldForSite(fieldName, site)
			for usageName in usageNames:
				# get usage
				usage = getUsageForField(usageName, field)
				# would have created it if didn't exist or updated it so I think we good

		# 	ET.SubElement(site, 'field')
		# fields = [value.strip() for value in fields.split(';')]
		# usages = [value.strip() for value in usages.split(';')]
		# # next, we add all the fields and usages
		# for field in fields:
		# 	addField(field)
		# for usage in usages:
		# 	addUsage(usage)
		# next we add the fields and usages to the site

		# TODO: validate input contains no xml-banned characters?
		# parse fields and uses
		# then store in db for address
		# catches exception which returns submit with error=True
		# otherwise returns void
		return 'GREEN'
	except Exception as e:
		return False
	
def addUser(username):
	newUser = ET.SubElement(elem_users, 'user')
	newUser.text = username

def getSite(addr):	 # done, untested
	for site in elem_sites.findall('site'):
		if site.attrib['addr'] == addr:
			return site
	# Program flow reached here so no site found
	# Create site
	newSite = ET.SubElement(elem_sites, 'site', {'addr':addr})
	return newSite


if __name__ == '__main__':
	app.run(debug=True)

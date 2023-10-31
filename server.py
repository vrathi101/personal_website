from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name=None):
	return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('thankyou.html')
		except:
			return 'Did not save to database'
	else:
		return 'something went wrong. try again'

def write_to_csv(data):
	with open('database.csv', newline='',mode='a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

def write_to_txt(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email},{subject},{message}')

# @app.route('/index.html')
# def my_index():
# 	return render_template('index.html')

# @app.route('/works.html')
# def my_works():
# 	return render_template('works.html')

# @app.route('/about.html')
# def about():
# 	return render_template('about.html')

# @app.route('/contact.html')
# def my_contact():
# 	return render_template('contact.html')





# # @app.route('/<username>')
# # def hello_world(username=None):
# # 	return render_template('index.html', name=username)

# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
# 	return render_template('intro_index.html', name=username, post_id=post_id)

# @app.route('/intro_about.html')
# def about():
# 	return render_template('about.html')

# @app.route('/blog')
# def blog():
# 	return 'these are my thoughts on blogs'

# @app.route('/blog/2020/dogs')
# def blog2():
# 	return 'this is my dog'
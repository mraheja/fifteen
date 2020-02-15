from flask import Flask, render_template, request
from random import choice

web_site = Flask(__name__)

number_list = [
	100, 101, 200, 201, 202, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
	416, 417, 418, 421, 422, 423, 424, 425, 426,
	429, 431, 444, 450, 451, 500, 502, 503, 504, 506, 507, 508, 509, 510, 511, 599
]

@web_site.route('/')
@web_site.route('/index.html')
@web_site.route('/home')
def index():
  return open('templates/index.html').read()

@web_site.route('/generic')
def index2():
  return open('templates/generic.html').read()

@web_site.route('/elements')
def elements():
  return render_template('elements.html')

@web_site.route('/user/', defaults={'username': None})
@web_site.route('/user/<username>')
def generate_user(username):
	if not username:
		username = request.args.get('username')

	if not username:
		return 'Sorry error something, malformed request.'

	return render_template('static/personal_user.html', user=username)

@web_site.route('/page')
def random_page():
  return render_template('static/page.html', code=choice(number_list))

@web_site.route('/matches', defaults={'username': None})
@web_site.route('/matches?<username>')
def matches(username):
  if not username:
 		username = request.args.get('username')

  # results = # some other method that returns a dictionary
  # pass in user id, display match

  return render_template('matches.html', header = username)

@web_site.route('/base')
def base():
  return render_template('base.html')


web_site.run(host='0.0.0.0', port=8080)
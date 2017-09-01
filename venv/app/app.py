from flask import Flask, render_template as render
from flask_orator import Orator
from orator.orm import belongs_to, has_many

app  = Flask(__name__)
app.config['ORATOR_DATABASES'] = {
	'development':{
		'driver'	: 'postgres',
		'port'		: 5433,
		'host'		: 'localhost',
		'database'	: 'flask_db',
		'user'		: 'flask_db',
		'password'	: 'flask123',
		'prefix'	: ''
	}	
}

db = Orator(app)


class Users(db.Model):
	__fillable__ = ['name', 'email', 'password', 'phone', 'gender']

	@has_many('user_id')
	def posts(self):
		return Posts

	def __repr__(self):
		return '<User %r>' % self.name

class Posts(db.Model):
	__fillable__ = ['title', 'content']

	@belongs_to
	def users(self):
		return Users


posts = db.table('posts').get()
users = db.table('users').get()

@app.route('/')
def index_page():
	return render('index_page.html', users=users, posts=posts)

@app.route('/login')
def login_page():
	return render('login_page.html')

@app.route('/signup')
def signup_page():
	return render('signup_page.html')

@app.route('/posts')
def posts_page():
	data = posts.users().first()
	return render('posts_page.html', data=data)

if __name__ == '__main__':
	app.run(debug=True)


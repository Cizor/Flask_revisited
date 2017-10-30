from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = { 'name' : 'Cizor'}
	posts = [
				{
					'author' : {'nickname' : 'Amrit'},
					'body' : 'I am a developer'
				},
				{
					'author' : {'nickname' : 'Mantoo'},
					'body' : 'I am a God'
				}
			]
	return render_template('index.html',title='Home',user=user,posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenId= "%s", remember_me= %s' % (form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html',title='Sign In',form=form,providers=app.config['OPENID_PROVIDERS'])

@lm.user_decorator
def load_user(id):
	return User.query.get(int(id))

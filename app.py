from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
	return '<h1>Home</h1>'

@app.route('/signin',methods=['GET'])
def signin_from():
	return '''<from action="/signin" method="post">
			  <p><input name="username"/></p>
			  <p><input name="password"/></p>
			  <p><button type="submit">Sign In</button></p>
			  </from>'''
@app.route('/signin',method=['POST'])
def signin():
	#需要从request对象中读取表单内容：
	if request.form['username']=='admin' and request.form['password']=='password':
		return '<h3>hello,admin!</h3>'
	return '<h3>bad username or password</h3>'

if __name__ == '__main__':
	app.run()

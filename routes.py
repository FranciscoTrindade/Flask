from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/vantagens')
def vantagens():
	return render_template('vantagens.html')
	
@app.route('/desvantagens')
def desvantagens():
	return render_template('desvantagens.html')
	
if __name__ == '__main__':
	app.run(debug=True)
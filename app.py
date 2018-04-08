from flask import Flask, render_template
app = Flask(__name__)

d = {'1': {
	'text':'Hello World',
	'htext':'!שלום ,עולם',
	'id':'line1',
	'parent':'none'},

	'2': {
	'text':'Goodbye World',
	'htext':'!שלום ,עולם',
	'id':'line2',
	'parent':'line1'}
}

@app.route('/')
def mainpage():
   return render_template('index.html', page = d)

if __name__ == '__main__':
   app.run()


   
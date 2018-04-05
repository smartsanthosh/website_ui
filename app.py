from flask import Flask,render_template,jsonify
from mongoengine import connect
connect(
    db='website_ui',
    username='admin',
    password='admin123',
    host='mongodb://admin:admin123@ds131384.mlab.com:31384/website_ui'
)

app=Flask(__name__)

@app.route("/")
def home():
	return render_template('index.html')
@app.route("/signup")
def signup():
	print(request.form)
	return jsonify(response="success")
if __name__=="__main__":
	app.run(debug=True)
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def Hello():
	return render_template("home.html")

@app.route("/trend")
def trend():
	return render_template("trending.html")

@app.route("/toprated")
def toprated():
	return render_template("toprated.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080)
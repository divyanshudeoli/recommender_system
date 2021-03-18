from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def Hello():
	return render_template("home.html")
if __name__ == '__main__':
    app.run(debug=True)
    TEMPLATES_AUTO_RELOAD=True
from flask import Flask,render_template
from user_routes import user_routes

app = Flask(__name__)
app.register_blueprint(user_routes, url_prefix="/user")

@app.route("/" , methods = ["GET"])
def test():
	return "Hello World!"

if __name__ == "__main__":
	print("Starting app")
	app.run(port = 8080,debug = True)

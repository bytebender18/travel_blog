from flask import Blueprint,render_template,jsonify
from repository import user_repository

user_routes = Blueprint("user_route",__name__)

@user_routes.route("/username/<string:username>",methods = ["GET"])
def get_by_username(username):
	user = user_repository.get_by_username(username)
	if(user is None):
		return jsonify({"Error":"No user found"}),404
	return jsonify(user),200




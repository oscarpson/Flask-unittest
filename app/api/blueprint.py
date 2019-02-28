from flask import Blueprint ,request, jsonify

hello_route = Blueprint("hello", __name__, url_prefix="/api/v1/")

@hello_route.route('/intro')
def intro():
    return "start blueprint api"
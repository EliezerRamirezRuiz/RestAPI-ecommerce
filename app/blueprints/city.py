from flask import Blueprint


city_blueprint = Blueprint('city', __name__, url_prefix="/city")


@city_blueprint.route('/')
def get_city():
    return "a"
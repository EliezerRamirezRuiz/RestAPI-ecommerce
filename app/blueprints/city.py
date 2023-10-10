from flask import Blueprint


city_blueprint = Blueprint('city', __name__)


@city_blueprint.route('/<>int:id')
def get_city():
    pass
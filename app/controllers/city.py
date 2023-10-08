from flask import Blueprint


city = Blueprint('city', __name__)


@city.route('/<>int:id')
def get_city():
    pass
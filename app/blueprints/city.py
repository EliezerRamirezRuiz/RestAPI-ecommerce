from flask import Blueprint


city = Blueprint('city', __name__)


@city.route('/')
def index():
    pass
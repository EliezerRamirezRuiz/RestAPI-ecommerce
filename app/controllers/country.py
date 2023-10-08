from flask import Blueprint


country = Blueprint('country', __name__)


@country.route('/')
def get_country():
    pass
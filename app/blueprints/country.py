from flask import Blueprint


country_blueprint = Blueprint('country', __name__)


@country_blueprint.route('/')
def get_country():
    pass
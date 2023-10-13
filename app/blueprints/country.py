from flask import Blueprint


country_blueprint = Blueprint('country', __name__, url_prefix="/country")


@country_blueprint.route('/')
def get_country():
    pass
from flask import Blueprint


brand_blueprint = Blueprint('brand', __name__, url_prefix="/brand")


@brand_blueprint.route('/<int:id>')
def get_brand(id):
    pass
from flask import Blueprint


category_blueprint = Blueprint('category', __name__, url_prefix="/category")


@category_blueprint.route('/<int:id>')
def get_category(id):
    pass
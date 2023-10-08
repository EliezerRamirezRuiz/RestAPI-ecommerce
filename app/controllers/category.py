from flask import Blueprint


category = Blueprint('category', __name__)


@category.route('/<int:id>')
def get_category(id):
    pass
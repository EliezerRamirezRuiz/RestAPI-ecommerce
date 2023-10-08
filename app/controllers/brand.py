from flask import Blueprint


brand = Blueprint('brand', __name__)


@brand.route('/<int:id>')
def get_brand(id):
    pass
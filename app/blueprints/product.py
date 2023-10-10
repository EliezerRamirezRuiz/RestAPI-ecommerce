from flask import Blueprint


product_blueprint = Blueprint('product', __name__)


@product_blueprint.route('/')
def get_product():
    pass
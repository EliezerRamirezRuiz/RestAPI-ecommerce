from flask import Blueprint


product = Blueprint('product', __name__)


@product.route('/')
def get_product():
    pass
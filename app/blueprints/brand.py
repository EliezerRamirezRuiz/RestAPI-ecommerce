from flask import Blueprint


brand = Blueprint('brand', __name__)


@brand.route('/')
def index():
    pass
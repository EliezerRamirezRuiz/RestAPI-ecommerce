from flask import Blueprint


category = Blueprint('category', __name__)


@category.route('/')
def index():
    pass
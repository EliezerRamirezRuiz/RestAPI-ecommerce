from flask import Blueprint


order = Blueprint('order', __name__)


@order.route('/')
def index():
    pass
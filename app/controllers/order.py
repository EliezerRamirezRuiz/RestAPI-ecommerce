from flask import Blueprint


order = Blueprint('order', __name__)


@order.route('/')
def get_order():
    pass
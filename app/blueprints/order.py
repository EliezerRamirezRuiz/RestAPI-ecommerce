from flask import Blueprint


order_blueprint = Blueprint('order', __name__)


@order_blueprint.route('/')
def get_order():
    pass
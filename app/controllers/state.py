from flask import Blueprint


state = Blueprint('state', __name__)


@state.route('/')
def get_state():
    pass
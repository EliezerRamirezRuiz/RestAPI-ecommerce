from flask import Blueprint


adress = Blueprint('adress', __name__)


@adress.route('/')
def index():
    pass
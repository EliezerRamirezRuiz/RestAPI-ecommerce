from flask import Blueprint


adress = Blueprint('adress', __name__)


@adress.route('/<int:id>')
def get_adress(id):
    pass
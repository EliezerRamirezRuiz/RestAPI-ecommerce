from flask import Blueprint
from flask import jsonify
from json import dumps

from ..models import AddressModel
from ..services import AddressService


address_blueprint = Blueprint('adress', __name__, url_prefix="/address")



@address_blueprint.route('/<int:id>')
def get_adress(id: int):
    try:
        address_service = AddressService
        return jsonify(
        )

    except Exception as ex:
        return jsonify(
            {
                "error": ex
            }
        )


@address_blueprint.route('/create')
def post_address():
    try:
        address_service = AddressService()
        address = AddressModel(
                name = "Sirio",
                number = 4022,
                city_id = 1,
                state_id = 1,
                country_id = 1
            )
        address_service.create_address(address=address)
        return "hello"
    
    except Exception as ex:
        print(ex)
        return f"error: {ex}"
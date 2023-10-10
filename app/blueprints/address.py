from flask import Blueprint
from flask import jsonify

from ..models import db
from ..repositories import AddressRepository


address_blueprint = Blueprint('adress', __name__)
address_repository = AddressRepository(db)


@address_blueprint.route('/address/<int:id>')
def get_adress(id):
    try:
        address = address_repository.find_by_id(id)
        return jsonify(
            {
                "response": "OK",
                "status_code": 200,
                "address": address
            }
        )

    except Exception as ex:
        return jsonify(
            {
                "error": ex
            }
        )

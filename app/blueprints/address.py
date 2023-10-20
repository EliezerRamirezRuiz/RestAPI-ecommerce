from flask import Blueprint, request
from flask import jsonify

from ..models import AddressModel
from ..services import AddressService


address_blueprint = Blueprint('adress', __name__, url_prefix="/address")


@address_blueprint.route('/<int:id>', methods=["GET"])
def get(id: int):
    try:
        if request.method == "GET":
            address_service = AddressService()
            address = address_service.get_by_id(id)

            if address is not None:
                return jsonify(
                    success=True,
                    message="data founded",
                    data=address,
                )

    except Exception as ex:
        return jsonify(
            error="data not found"
        )


@address_blueprint.route('/', methods=["POST"])
def post():
    try:
        if request.method == "POST":
            address_service = AddressService()
            address = AddressModel(
                name=request.json['name'],
                number=int(request.json['number']),
                city_id=int(request.json['city_id']),
                state_id=int(request.json['state_id']),
                country_id=int(request.json['country_id'])
            )

            address_created = address_service.create_address(address=address)
            return jsonify(
                success=True,
                message="data created",
                data=address_created
            )

    except Exception:
        return jsonify(
            error="couldn't be created"
        )


@address_blueprint.route('/<int:id>', methods=["PUT"])
def update(id: int):
    try:
        if request.method == "PUT":
            address = request.json['address']
            address_service = AddressService()
            print(address)
            response = address_service.update_address(
                id, 
                address)
            return jsonify(data=response)

    except Exception as ex:
        print(ex)
        return f"Error: {ex}"

from flask import Blueprint
from flask import jsonify
from flask import request


from ..models import AddressModel
from ..services import AddressService


address = Blueprint('adress', __name__, url_prefix="/address")


@address.route('/<int:id>', methods=["GET"])
def get_by_id(id: int):
    try:
        if request.method == "GET":
            service = AddressService()
            model = service.get_by_id(id)

            if model is not None: 
                return jsonify(
                    success=True,
                    message="data founded",
                    data=model,
                )

    except Exception as ex:
        print(ex)
        return jsonify(
            error="data not found"
        )



@address.route('/', methods=["POST"])
def post():
    try:
        if request.method == "POST":
            service = AddressService()
            address = AddressModel(
                name=request.json['name'],
                number=int(request.json['number']),
                city_id=int(request.json['city_id']),
                state_id=int(request.json['state_id']),
                country_id=int(request.json['country_id'])
            )

            address_created = service.create_model(model=address)
            return jsonify(
                success=True,
                message="data created",
                data=address_created
            )

    except Exception:
        return jsonify(
            error="couldn't be created"
        )


@address.route('/<int:id>', methods=["PUT"])
def update(id: int):
    try:
        if request.method == "PUT":
            address = request.json['address']
            service = AddressService()
            response = service.update_model(
                id = id, 
                model = address)
            return jsonify(data=response)

    except Exception as ex:
        return f"Error: {ex}"

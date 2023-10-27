from flask import Blueprint
from flask import jsonify
from flask import request

from ..services import BrandService
from ..models import BrandModel


brand = Blueprint('brand', __name__, url_prefix="/brand")


@brand.route('/<int:id>', methods=["GET"])
def get_by_id(id: int):
    try:
        if request.method == "GET":
            service = BrandService()
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



@brand.route('/', methods=["POST"])
def post():
    try:
        if request.method == "POST":
            service = BrandService()
            address = BrandModel(
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


@brand.route('/<int:id>', methods=["PUT"])
def update(id: int):
    try:
        if request.method == "PUT":
            address = request.json['address']
            service = BrandService()
            response = service.update_model(
                id = id, 
                model = address)
            return jsonify(data=response)

    except Exception as ex:
        return f"Error: {ex}"
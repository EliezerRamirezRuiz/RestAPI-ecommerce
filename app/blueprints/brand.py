from flask import Blueprint, request, jsonify

from ..repositories import BrandRepository


brand = Blueprint('brand', __name__, url_prefix="/brand")


@brand.route('/<int:id>')
def get_brand(id):
    try:
        if request.method == "GET":
            address_service = BrandRepository()
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
from flask import Blueprint
from flask import jsonify


handler_error_blueprint = Blueprint("error", __name__)


@handler_error_blueprint.errorhandler(404)
def resource_not_found(e):
    return jsonify(
        error="data not found"
    ), 404


@handler_error_blueprint.errorhandler(500)
def resource_not_found(e):
    return jsonify(
        error="internal server",
        ), 500

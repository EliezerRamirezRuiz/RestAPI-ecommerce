from flask import Flask


def load_blueprint(app:Flask) -> None:
    """ function to load Blueprints"""
    from .address import address_blueprint
    from .brand import brand_blueprint
    from .category import category_blueprint
    from .city import city_blueprint
    from .country import country_blueprint
    from .order import order_blueprint
    from .product import product_blueprint
    from .state import state_blueprint
    from .user import user_blueprint
    from .swagger import swagger_ui_blueprint
    
    app.register_blueprint(address_blueprint)
    app.register_blueprint(brand_blueprint)
    app.register_blueprint(category_blueprint)
    app.register_blueprint(city_blueprint)
    app.register_blueprint(country_blueprint)
    app.register_blueprint(order_blueprint)
    app.register_blueprint(product_blueprint)
    app.register_blueprint(state_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(swagger_ui_blueprint)
    
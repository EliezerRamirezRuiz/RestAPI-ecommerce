import pytest
from .. import create_app


@pytest.fixture()
def app():
    app = create_app()
    
    app.config.update({
        "TESTING": True,
    })
        
    yield app
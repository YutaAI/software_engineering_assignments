from fastapi.testclient import TestClient
from ..main import app
from ..models import customers as model

client = TestClient(app)


def test_customers_route_registered():
    # Check that the customers route is registered
    paths = set(app.openapi()["paths"].keys())
    assert "/customers/" in paths


def test_create_customer_model():
    # simple model instantiation test
    data = {"name": "Alice", "email": "a@example.com", "phone": "555-1234", "address": "123 Main St"}
    cust_obj = model.Customer(**data)
    assert cust_obj.name == "Alice"
    assert cust_obj.email == "a@example.com"
    assert cust_obj.phone == "555-1234"

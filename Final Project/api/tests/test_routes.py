from ..main import app


def test_expected_routes_are_registered():
    paths = set(app.openapi()["paths"].keys())

    assert "/orders/" in paths
    assert "/orderdetails/" in paths
    assert "/sandwiches/" in paths
    assert "/recipes/" in paths
    assert "/resources/" in paths
    assert "/feedbacks/" in paths
    assert "/promotions/" in paths
    assert "/reports/summary" in paths
    assert "/reports/orders-by-status" in paths
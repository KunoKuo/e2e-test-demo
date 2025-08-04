import requests

def test_get_items():
    response = requests.get("http://localhost:5000/items")
    assert response.status_code == 200
    assert "item1" in response.json()

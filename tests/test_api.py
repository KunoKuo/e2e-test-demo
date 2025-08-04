import requests

def test_get_items():
    response = requests.get("http://127.0.0.1:5000/items")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "item1" in data
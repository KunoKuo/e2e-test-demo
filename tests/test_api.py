import requests

def test_get_items():
    response = requests.get("http://127.0.0.1:5000/items")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "item1" in data

def test_get_items_content():
    response = requests.get("http://127.0.0.1:5000/items")
    assert response.status_code == 200
    assert response.json() == ["item1", "item2", "item3"]

def test_get_items_header():
    response = requests.get("http://127.0.0.1:5000/items")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
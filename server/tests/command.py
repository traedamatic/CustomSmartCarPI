import requests


def test_command_route():
    response = requests.get("http://localhost:5000/command/forward")
    assert response.status_code == 200

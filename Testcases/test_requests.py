import requests

def test_get_request():
    url = "https://vnexpress.net"
    response = requests.get(url)
    try:
        print(response.json())
    except: print("Response is not in JSON format")

    assert response.status_code == 200

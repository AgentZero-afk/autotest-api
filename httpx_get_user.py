import httpx
import json
from tools.fakers import get_random_email
payload = {
        "email": get_random_email(),
        "password": "pass123123",
        "lastName": "test1",
        "firstName": "test2",
        "middleName": "test3"
    }
response = httpx.post('http://localhost:8000/api/v1/users', json=payload)
user_created_response = response.json()
print(json.dumps(response.json(), indent=4, ensure_ascii=False))
print(response.status_code)

login_payload = {
    "email": payload['email'],
    "password": payload['password']
}
login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print('login data', json.dumps(login_response_data, indent=4, ensure_ascii=False))

get_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}",
}
get_user_response = httpx.get(f'http://localhost:8000/api/v1/users/{user_created_response['user']['id']}',
headers=get_user_headers
)
get_user_response_data = get_user_response.json()
print('Get user data', json.dumps(get_user_response_data, indent=4, ensure_ascii=False))
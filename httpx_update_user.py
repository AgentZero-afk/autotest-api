import httpx
import json
from tools.fakers import get_random_email
auth_payload = {
        "email": get_random_email(),
        "password": "pass123123",
        "lastName": "test1",
        "firstName": "test2",
        "middleName": "test3"
    }
response = httpx.post('http://localhost:8000/api/v1/users', json=auth_payload)
user_created_response = response.json()
print(json.dumps(response.json(), indent=4, ensure_ascii=False))
print(response.status_code)

login_payload = {
    "email": auth_payload['email'],
    "password": auth_payload['password']
}
login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print('status code', login_response.status_code)
print('login data', json.dumps(login_response_data, indent=4, ensure_ascii=False))

patch_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
patch_payload = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
patch_response = httpx.patch(f'http://localhost:8000/api/v1/users/{user_created_response["user"]['id']}', headers=patch_headers,json=patch_payload)

patch_response_data = patch_response.json()
print('status code', patch_response.status_code)
print('patch response', json.dumps(patch_response_data, indent=4, ensure_ascii=False))
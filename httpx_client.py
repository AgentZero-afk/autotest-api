import httpx
import json



login_payload = {
    "email": "test@gmail.com",
    "password": "pass123"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('login data', json.dumps(login_response.json(), indent=4, ensure_ascii=False))

client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=100,
    headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
)

get_user_me_response = client.get("/api/v1/users/me")
get_user_me_response_data = get_user_me_response.json()
print("Get user me data:", json.dumps(get_user_me_response_data, indent=4, ensure_ascii=False))
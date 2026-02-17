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
print(json.dumps(response.json(), indent=4, ensure_ascii=False))
print(response.status_code)



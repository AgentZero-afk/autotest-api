from httpx import Response
from clients.api_client import APIClient
from typing import TypedDict
from clients.public_http_builder import get_public_http_client

class User(TypedDict):
    id: str
    email: str
    firstName: str
    lastName: str
    middleName: str


class RequestCreateUserDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    user: User



class PublicUsersClient(APIClient):
    """Клиент для взаимодействия с публичными ручками, не требующие авторизации"""
    def create_user_api(self, request: RequestCreateUserDict) -> Response:
        """Ручка для создания пользователя
            Принимает:
            :param request: Принимает RequestCreateUserDict(email,password,lastname,firstname,middlename)
            Возвращает:
            :return: ответ ручки post "/api/v1/users
            """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserResponseDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())
from httpx import Response
from clients.api_client import APIClient
from typing import TypedDict


class RequestCreateUserDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str



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

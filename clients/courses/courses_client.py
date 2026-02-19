from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict

class GetCoursesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка курсов
    """
    userId: str

class CreateCourseRequestDict(TypedDict):
    """Описание структуры запроса на создание курса"""
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFieldId: str
    createByUserId: str

class UpdateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление курса
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса по идентификатору.

        :param course_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Метод для создания курса
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, previewFieldId, createByUserId,
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Метод обновления курса по идентификатору
        :param course_id: Идентификатор курса
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса
        :param course_id: идентификатор курса
        :return: ответ с сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом
    :return: Готовый к использованию CoursesClient
    """
    return CoursesClient(client=get_private_http_client(user))
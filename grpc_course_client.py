import grpc

import course_service_pb2
import course_service_pb2_grpc


def run():
    # Устанавливаем соединение с gRPC-сервером
    channel = grpc.insecure_channel('localhost:50051')

    # Создаём стаб (клиент) для сервиса CourseService
    stub = course_service_pb2_grpc.CourseServiceStub(channel)

    # Формируем запрос
    request = course_service_pb2.GetCourseRequest(course_id="api-course")

    # Вызываем метод GetCourse и получаем ответ
    response = stub.GetCourse(request)

    # Выводим ответ в консоль
    print(response)


if __name__ == "__main__":
    run()
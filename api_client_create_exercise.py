from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, RequestCreateUserDict
from tools.fakers import get_random_email

# 1. Создать пользователя
public_users_client = get_public_users_client()

create_user_request = RequestCreateUserDict(
    email=get_random_email(),
    password='string',
    lastName='string',
    firstName='string',
    middleName='string'
)
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

# 2. Загрузить файл
files_client = get_files_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename='image.png',
    directory='courses',
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# 3. Создать курс
courses_client = get_courses_client(authentication_user)

create_course_request = CreateCourseRequestDict(
    title='Python',
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# 4. Создать задание
exercises_client = get_exercises_client(authentication_user)

create_exercise_request = CreateExerciseRequestDict(
    title='Exercise 1',
    courseId=create_course_response['course']['id'],
    maxScore=100,
    minScore=10,
    orderIndex=0,
    description='First exercise',
    estimatedTime='1 hour'
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)

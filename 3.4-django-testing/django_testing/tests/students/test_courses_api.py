import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


#fixtures:

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


#tests:

@pytest.mark.django_db
def test_get_course_detail(client, courses_factory):
    #тест на получение информации о конкретном курсе
    courses_factory(name='Основы SQL')
    response = client.get('/api/v1/courses/1/')
    data = response.json()
    assert response.status_code == 200
    assert data['name'] == 'Основы SQL'

@pytest.mark.django_db
def test_get_courses(client, courses_factory):
    #тест на получение информации о всех курсах
    courses_factory(_quantity=20)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 20

@pytest.mark.django_db
def test_filter_course_by_id(client, courses_factory):
    #тест на фильтр курсов по id
    courses = courses_factory(_quantity=5)
    response = client.get(f'/api/v1/courses/?id={courses[2].id}')
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['id'] == courses[2].id

@pytest.mark.django_db
def test_filter_course_by_name(client, courses_factory):
    #тест на фильтр курсов по name
    Course.objects.create(name='Основы SQL')
    Course.objects.create(name='Python в веб-разработке')
    Course.objects.create(name='Продвинутый курс по C++')
    response = client.get('/api/v1/courses/?name=Python в веб-разработке')
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['name'] == 'Python в веб-разработке'

@pytest.mark.django_db
def test_create_course(client):
    #тест на добавление нового курса
    data = {'name': 'Создание веб-приложений на Django'}
    response = client.post('/api/v1/courses/', data=data, format='json')
    new_course = response.json()
    assert response.status_code == 201
    assert new_course['name'] == 'Создание веб-приложений на Django'

@pytest.mark.django_db
def test_patch_course(client, courses_factory):
    #тест на изменение данных курса
    course = courses_factory(name='Новый курс')
    data = {'name': 'Frontend разработка'}
    response = client.patch(f'/api/v1/courses/{course.id}/', data=data, format='json')
    edit_course = response.json()
    assert response.status_code == 200
    assert edit_course['name'] != 'Новый курс'
    assert edit_course['name'] == 'Frontend разработка'

@pytest.mark.django_db
def test_delete_course(client, courses_factory):
    #тест на удаление курса
    course = courses_factory(name='Тестировщик ПО')
    delete_response = client.delete(f'/api/v1/courses/{course.id}/')
    get_response = client.get(f'/api/v1/courses/{course.id}/')
    assert delete_response.status_code == 204
    assert get_response.status_code != 200

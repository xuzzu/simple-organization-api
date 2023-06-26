from django.test import TestCase, Client
from django.urls import reverse
from django.utils.datetime_safe import datetime
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Person, Department, Position, Task
from .serializers import PersonSerializer, DepartmentSerializer, PositionSerializer, TaskSerializer


""""
Набор стандартных юнит тестов для тестирования CRUD операций. 
"""

class PersonTest(APITestCase):
    def setUp(self):
        self.person1 = Person.objects.create(name='John')
        self.person2 = Person.objects.create(name='Jane')
        self.valid_payload = {'name': 'Bob'}
        self.invalid_payload = {'name': ''}
        self.client = APIClient()

    def test_get_all_people(self):
        response = self.client.get(reverse('person-list'))
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_person(self):
        response = self.client.get(reverse('person-detail', kwargs={'pk': self.person1.pk}))
        person = Person.objects.get(pk=self.person1.pk)
        serializer = PersonSerializer(person)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_person(self):
        response = self.client.post(reverse('person-list'), data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_person(self):
        response = self.client.post(reverse('person-list'), data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_person(self):
        payload = {'name': 'Jack'}
        response = self.client.put(reverse('person-detail', kwargs={'pk': self.person1.pk}), data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_person(self):
        response = self.client.delete(reverse('person-detail', kwargs={'pk': self.person1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class DepartmentTest(APITestCase):
    def setUp(self):
        self.department1 = Department.objects.create(dep_name='Finance')
        self.department2 = Department.objects.create(dep_name='Sales')
        self.valid_payload = {'dep_name': 'Marketing'}
        self.invalid_payload = {'dep_name': ''}
        self.client = APIClient()

    def test_get_all_departments(self):
        response = self.client.get(reverse('department-list'))
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_department(self):
        response = self.client.get(reverse('department-detail', kwargs={'pk': self.department1.pk}))
        department = Department.objects.get(pk=self.department1.pk)
        serializer = DepartmentSerializer(department)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_department(self):
        response = self.client.post(reverse('department-list'), data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_department(self):
        response = self.client.post(reverse('department-list'), data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_department(self):
        payload = {'dep_name': 'Marketing'}
        response = self.client.put(reverse('department-detail', kwargs={'pk': self.department1.pk}), data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_department(self):
        response = self.client.delete(reverse('department-detail', kwargs={'pk': self.department1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PositionTest(APITestCase):
    def setUp(self):
        self.department1 = Department.objects.create(dep_name='Finance')
        self.position1 = Position.objects.create(pos_name='Manager', department=self.department1)
        self.position2 = Position.objects.create(pos_name='Assistant', department=self.department1)
        self.valid_payload = {'pos_name': 'Analyst', 'department': self.department1.pk, 'salary': 5000}
        self.invalid_payload = {'pos_name': '', 'department': self.department1.pk, 'salary': 5000}
        self.client = APIClient()

    def test_get_all_positions(self):
        response = self.client.get(reverse('position-list'))
        positions = Position.objects.all()
        serializer = PositionSerializer(positions, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_position(self):
        response = self.client.get(reverse('position-detail', kwargs={'pk': self.position1.pk}))
        position = Position.objects.get(pk=self.position1.pk)
        serializer = PositionSerializer(position)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_position(self):
        response = self.client.post(reverse('position-list'), data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_position(self):
        response = self.client.post(reverse('position-list'), data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_position(self):
        payload = {'pos_name': 'Analyst', 'department': self.department1.pk, 'salary': 6000}
        response = self.client.put(reverse('position-detail', kwargs={'pk': self.position1.pk}), data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_position(self):
        response = self.client.delete(reverse('position-detail', kwargs={'pk': self.position1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TaskTest(APITestCase):
    def setUp(self):
        self.task1 = Task.objects.create(task_name='Organize files', deadline='2022-01-01T00:00:00Z')
        self.task2 = Task.objects.create(task_name='Send emails', deadline='2022-02-01T00:00:00Z')
        self.valid_payload = {'task_name': 'Prepare presentation', 'deadline': '2022-03-01T00:00:00Z'}
        self.invalid_payload = {'task_name': '', 'deadline': '2022-03-01T00:00:00Z'}
        self.client = APIClient()

    def test_get_all_tasks(self):
        response = self.client.get(reverse('task-list'))
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_task(self):
        response = self.client.get(reverse('task-detail', kwargs={'pk': self.task1.pk}))
        task = Task.objects.get(pk=self.task1.pk)
        serializer = TaskSerializer(task)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_task(self):
        response = self.client.post(reverse('task-list'), data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_task(self):
        response = self.client.post(reverse('task-list'), data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_task(self):
        payload = {'task_name': 'Prepare presentation', 'deadline': '2022-04-01T00:00:00Z'}
        response = self.client.put(reverse('task-detail', kwargs={'pk': self.task1.pk}), data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(reverse('task-detail', kwargs={'pk': self.task1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)




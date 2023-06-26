from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

"""
Этот файл содержит определения моделей для базы данных. 
- Класс Person представляет собой запись о человеке с его 
фотографией, именем и адресом электронной почты. 
- Класс Department использует MPTT для создания иерархии отделов и удобного прохода по дереву. 
- Класс Position также использует MPTT и связывает запись о человеке с отделом и должностью, а также содержит 
информацию о зарплате. 
- Класс Task представляет собой задачу с именем и дедлайном. 
- Класс PersonTask является бридж таблицей и связывает работника и задачу.
"""

class Person(models.Model):
    photo = models.BinaryField()
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)


class Department(MPTTModel):
    dep_name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


class Position(MPTTModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    salary = models.IntegerField(null=True)
    department = TreeForeignKey(Department, on_delete=models.CASCADE, null=True)
    pos_name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


class Task(models.Model):
    task_name = models.CharField(max_length=255)
    deadline = models.DateTimeField()


class PersonTask(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)

    class Meta:
        unique_together = ('person', 'task')

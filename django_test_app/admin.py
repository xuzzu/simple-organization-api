from django.contrib import admin

from .models import Person, Department, Position, Task, PersonTask

admin.site.register(Person)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Task)
admin.site.register(PersonTask)
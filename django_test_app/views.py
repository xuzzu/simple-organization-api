from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Person, Department, Position, Task, PersonTask
from .serializers import PersonSerializer, DepartmentSerializer, PositionSerializer, TaskSerializer, \
    PersonTaskSerializer, PersonSummarySerializer, OrganizationSerializer

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PositionList(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class PersonTaskList(generics.ListCreateAPIView):
    queryset = PersonTask.objects.all()
    serializer_class = PersonTaskSerializer


class PersonTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonTask.objects.all()
    serializer_class = PersonTaskSerializer


class OrganizationStructureView(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.prefetch_related(
        'children', 'position_set').filter(parent=None)
    serializer_class = OrganizationSerializer

    def get_actions(self):
        actions = super().get_actions()
        del actions['create']
        del actions['update']
        del actions['partial_update']
        del actions['destroy']
        return actions

class PersonSummaryView(APIView):
    def get(self, request, person_id):
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)

        departments = Department.objects.filter(position__person=person)
        positions = Position.objects.filter(person=person)
        tasks = Task.objects.filter(persontask__person=person)
        department_names = [dept.dep_name for dept in departments]
        position_names = [pos.pos_name for pos in positions]
        salary = [pos.salary for pos in positions]
        task_names = [task.task_name for task in tasks]
        task_deadlines = [task.deadline for task in tasks]

        summary_data = {
            'id': person.id,
            'name': person.name,
            'photo': person.photo,
            'departments': department_names,
            'positions': position_names,
            'salary': salary,
            'tasks': task_names,
            'task_deadlines': task_deadlines,
        }

        serializer = PersonSummarySerializer(summary_data)
        return Response(serializer.data)

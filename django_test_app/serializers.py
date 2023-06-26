from rest_framework import serializers
from .models import Person, Department, Position, Task, PersonTask


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PersonRecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        exclude = ('photo', 'email')


class PositionRecSerializer(serializers.ModelSerializer):
    person = PersonRecSerializer()

    class Meta:
        model = Position
        fields = ('id', 'pos_name', 'department', 'person')


class DepartmentSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        required=False
    )

    class Meta:
        model = Department
        fields = ('id', 'dep_name', 'parent')


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'pos_name', 'department', 'salary')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class PersonTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonTask
        fields = ('person', 'task')

class PersonSummarySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    photo = serializers.CharField()
    departments = serializers.ListField(child=serializers.CharField())
    salary = serializers.ListField(child=serializers.IntegerField())
    positions = serializers.ListField(child=serializers.CharField())
    tasks = serializers.ListField(child=serializers.CharField())
    task_deadlines = serializers.ListField(child=serializers.DateTimeField())


class OrganizationSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    positions = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('id', 'dep_name', 'parent_id', 'positions', 'children')

    def get_children(self, obj):
        queryset = obj.get_children()
        serializer = self.__class__(queryset, many=True)
        return serializer.data

    def get_positions(self, obj):
        queryset = Position.objects.filter(department=obj)
        serializer = PositionRecSerializer(queryset, many=True)
        return serializer.data

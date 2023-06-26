from django.urls import path
from .views import PersonList, PersonDetail, DepartmentList, DepartmentDetail, \
    PositionList, PositionDetail, TaskList, TaskDetail, PersonTaskList, PersonTaskDetail, PersonSummaryView, OrganizationStructureView

urlpatterns = [
    path('person/', PersonList.as_view(), name='person-list'),
    path('person/<int:pk>/', PersonDetail.as_view(), name='person-detail'),
    path('department/', DepartmentList.as_view(), name='department-list'),
    path('department/<int:pk>/', DepartmentDetail.as_view(), name='department-detail'),
    path('position/', PositionList.as_view(), name='position-list'),
    path('position/<int:pk>/', PositionDetail.as_view(), name='position-detail'),
    path('task/', TaskList.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('person-task/', PersonTaskList.as_view(), name='person-task-list'),
    path('person-task/<int:pk>/', PersonTaskDetail.as_view(), name='person-task-detail'),
    path('person/<int:person_id>/summary/', PersonSummaryView.as_view(), name='person-summary'),
    path('organization-structure/', OrganizationStructureView.as_view({'get': 'list'}), name='organization-structure'),
    ]
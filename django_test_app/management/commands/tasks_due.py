from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from django_test_app.models import Task, PersonTask

SENDING_EMAIL = 'from@example.com'

class Command(BaseCommand):
    help = 'Sends email notifications for tasks that are due'

    def handle(self, *args, **options):
        tasks = Task.objects.filter(deadline__lte=timezone.now())
        for task in tasks:
            persons = PersonTask.objects.filter(task=task).values_list('person__email', flat=True).distinct()
            for person_email in persons:
                send_mail(
                    f'Task "{task.task_name}" is due',
                    f'Task "{task.task_name}" is due on {task.deadline}.',
                    SENDING_EMAIL,
                    [person_email],
                    fail_silently=False,
                )
        self.stdout.write(self.style.SUCCESS(f'Successfully sent {len(tasks)} task notifications.'))
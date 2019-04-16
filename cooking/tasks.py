import time

from celery import shared_task
from datetime import timedelta

from celery.schedules import crontab
from django.core.mail import send_mail

from cooking.models import User


@shared_task
def test_task():
    time.sleep(10)
    return 1


@shared_task
def test_sum(arg1, arg2):
    time.sleep(3)
    return arg1 + arg2


@shared_task
def send_mails():
    emails = User.objects.all().values_list('email', flat=True)
    send_mail('Test_mail', 'Some messages', 'admin@cooking.io', emails)
    print('here')


SCHEDULE = {
    'send_test_mail': {
        'task': 'cooking.tasks.send_mails',
        'args': (),
        'options': {},
        'schedule': timedelta(seconds=5)
    }
}

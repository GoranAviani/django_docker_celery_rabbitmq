from __future__ import absolute_import, unicode_literals
from django_docker_celery_rabbitmq.celery import app 
from celery import shared_task

#periodic task
@shared_task
def periodic_task():
    print("This is a test Task!"))
   
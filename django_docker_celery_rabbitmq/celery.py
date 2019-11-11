from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_docker_celery_rabbitmq.settings')

app = Celery('django_docker_celery_rabbitmq',
             broker='amqp://guest@localhost//',
             backend='amqp://guest@localhost//',
             )

app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
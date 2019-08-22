import os

import django
from celery import Celery, shared_task
from celery.schedules import crontab
from celery.signals import task_success
from django.conf import settings
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_demo.settings')
django.setup()

app = Celery('django_celery_demo')
app.config_from_object('django.conf:settings')   # celery app 加载 settings中的配置

app.now = timezone.now   # 设置时间时区和django一样

# 加载每个django app下的tasks.py中的task任务
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# 这个是硬编码的定时任务
app.conf.beat_schedule = {
    'aa': {
        'task': 'add',
        'schedule': crontab(minute="*/1"),
        'args': (2, 4)
    },
    
}


# 这个一个task
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# 异步执行这个task
debug_task.delay()

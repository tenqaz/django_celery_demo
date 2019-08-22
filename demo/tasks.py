from celery import shared_task


@shared_task(name="add")
def add(a, b):
    return int(a) + int(b)

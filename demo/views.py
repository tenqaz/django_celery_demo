from django.http import HttpResponse

from demo.tasks import add as add_task


def add(request):

    a = request.GET["a"]
    b = request.GET["b"]

    add_task.delay(a, b)
    return HttpResponse("success")

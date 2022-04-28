from urllib.request import Request

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Article


# Create your views here.
def home(request: Request):
    # return HttpResponse("Hello World")
    # context: dict = {
    #     "username": "Amirhossein",
    #     "age": 27,
    #     "job": "Programmer"
    # }

    context: dict = {
        "articles": Article.objects.filter(status="p").order_by("-publish_datetime")
    }
    return render(request, "blog/home.html", context)

def api(request: Request):
    return JsonResponse({"title": "سلام دنیا"})

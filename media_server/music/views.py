from typing import Any

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request: Any) -> HttpResponse:
    return HttpResponse("yo")

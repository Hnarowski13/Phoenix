from django.http import HttpResponse
from django.shortcuts import render


def cooks(request):

    return render(request, 'cooks.html')
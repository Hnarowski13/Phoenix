from django.http import HttpResponse
from django.shortcuts import render


def finance(request):

    return render(request, 'finance.html')
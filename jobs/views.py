from django.http import HttpResponse
from django.shortcuts import render


def jobs(request):

    return render(request, 'jobs.html')
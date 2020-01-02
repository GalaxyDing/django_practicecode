from django.shortcuts import render

from App.models import Grade


def index(request):
    grades = Grade.objects.all()
    context = {
        'grades': grades
    }

    return render(request, 'index.html', context=context)

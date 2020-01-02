from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Student


def student_info(request):
    grade_name = request.GET.get('gradename')
    students = Student.objects.filter(s_grade__grade_name=grade_name)
    student_list = []
    for s in students:
        student_list.append(s)
    context = {
        'student_list': student_list,
        'grade_name': grade_name
    }

    return render(request, 'student_info.html', context=context)

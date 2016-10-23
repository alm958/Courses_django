from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Course

# Create your views here.
def add_course(request):
    if request.method == 'POST':
        result = Course.objects.add_course(name=request.POST['name'],description=request.POST['description'])
        if result[0] == False :
            for error_message in result[1] :
                messages.error(request, error_message)
        else :
            for success_message in result[1] :
                messages.success(request, success_message)
        return redirect(reverse( 'index' ) )

def index(request):
    all_courses = Course.objects.all_courses()
    context = {
    'all_courses' : all_courses
    }
    return render(request, 'courses/index.html', context )

def del_prompt(request, id):
    course = Course.objects.get(id=id)
    context = {
    'course' : course
    }
    return render(request, 'courses/delete_prompt.html', context )

def del_course(request, id):
    course = Course.objects.get(id=id)

    Course.objects.filter(id=id).delete()
    return redirect(reverse( 'index' ) )

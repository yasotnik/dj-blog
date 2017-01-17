from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Course, Lecture

from django.views import generic


class CoursesView(generic.ListView):
    template_name = 'courses/index.html'

    def get_queryset(self):
        return Course.objects.all()


class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/course.html'


class CourseCreate(CreateView):
    model = Course
    fields = ['name', 'teacher', 'length', 'field', 'course_logo']


class CourseUpdate(UpdateView):
    model = Course
    fields = ['name', 'teacher', 'length', 'field', 'course_logo']


class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:index')


class LectureCreate(CreateView):
    model = Lecture
    # print(course_pk)
    fields = ['course', 'file_type', 'lecture_name', 'lecture_url']
    success_url = reverse_lazy('courses:index')
    # success_url = reverse_lazy('courses:course_info', kwargs={'pk': course_pk})


class UserFormView(View):
    form_class = UserForm
    template_name = 'courses/registration.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # reg user
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('courses:index')

        return render(request, self.template_name, {'form': form})

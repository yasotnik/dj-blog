from django.conf.urls import url
from . import views


app_name = 'courses'


urlpatterns = [
    # URL for course list /courses
    url(r'^$', views.CoursesView.as_view(), name='index'),
    # URL for exact course /course/id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='course_info'),
    # URL for following the course
    url(r'^follow$', views.follow, name='follow'),
    # URL for following the course
    url(r'^unfollow$', views.un_follow, name='un_follow'),
]

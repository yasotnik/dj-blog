from django.conf.urls import url
from . import views


app_name = 'courses'


urlpatterns = [
    # URL for course list /courses
    url(r'^$', views.index, name='index'),
    # URL for exact course /course/id/
    url(r'^(?P<course_id>[0-9]+)/$', views.course_details, name='course_info'),
    # URL for following the course
    url(r'^follow$', views.follow, name='follow'),
    # URL for following the course
    url(r'^unfollow$', views.un_follow, name='un_follow'),
]

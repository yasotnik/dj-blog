from django.conf.urls import url
from . import views


urlpatterns = [
    # URL for course list /courses
    url(r'^$', views.index, name='index'),
    # URL for exact course /course/id/
    url(r'^(?P<course_id>[0-9]+)/$', views.course, name='course_info'),
]

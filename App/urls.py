from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^student_info/$', views.student_info),

]

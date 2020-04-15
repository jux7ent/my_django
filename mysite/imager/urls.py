from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.some_func, name='index'),
    path('<str:folder_name>/', views.detail, name='detail')
]

urlpatterns += staticfiles_urlpatterns()

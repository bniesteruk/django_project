from django.urls import path
from .views import MyDataView, views

urlpatterns = [
    path('', views.home, name='home'),
    path('django_project/', MyDataView.as_view(), name='django_project'),
]
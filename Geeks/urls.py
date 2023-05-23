from django.urls import path
from . import views
urlpatterns = [
    path('', views.formset_view, name='formset_view'),
]
from django.urls import path
from .views import HomePage

app_name = 'hodka'

urlpatterns = [
    path('', HomePage, name='home'),
]
from django.urls import path
from apps.views import index


urlpatterns = [
    path("", index, name="index")
]
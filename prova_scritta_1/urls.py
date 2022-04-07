from django.urls.conf import path

from .views import view_b
from .views import view_c
from .views import view_API

app_name="prova_scritta_1"

urlpatterns=[
    path("view_b",view_b,name="view_b"),
    path("view_c",view_c,name="view_c"),
    path("view_API",view_API,name="view_API")
]
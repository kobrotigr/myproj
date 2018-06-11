from django.urls import path
from .views import OrdCreate


urlpatterns = [
        path('new/', OrdCreate.as_view(), name='ord_new'),

]
from django.urls import path

from .views import LongPollView

urlpatterns = [
    path('longpoll/', LongPollView.as_view(), name='longpoll'),
]

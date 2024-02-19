from django.urls import path

from educa.auth.users.views import UserAdminView

urlpatterns = [
    path('login/',UserAdminView.as_view()),
]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('question/<int:pk>', views.question),
    path('teams', views.show_teams),
    path('change/<int:pk>', views.add_score)
]

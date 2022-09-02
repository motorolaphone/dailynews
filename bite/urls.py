from django.urls import path
from . import views

urlpatterns = [
    path('',views.general_news,name="news"),
    path('technology/', views.tech_news,name="tech_news"),
    path('sports/',views.sports_cricket,name="cricket"),
    path('feedback/',views.feedback,name="feedback"),
    path('about/',views.about,name="about"),
    path('education/',views.education,name="education"),
    path('health/',views.health,name="health"),
    path('football/',views.sports_football,name="football"),
    path('volleyball/',views.sports_volleyball,name="volleyball"),
    path('hockey/',views.sports_hockey,name="hockey")
    

]

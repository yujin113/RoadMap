from django.urls import path
import info.views
from . import views

urlpatterns = [
    path('mypage/', views.myPage, name="myPage"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio/projectcreate/', views.projectcreate, name='projectcreate'),
    path('portfolio/projectupdate/<int:project_id>', views.projectupdate, name='projectupdate'),
    path('portfolio/projectdelete/<int:project_id>', views.projectdelete, name='projectdelete'),
    path('portfolio/activitycreate/', views.activitycreate, name='activitycreate'),
    path('portfolio/activityupdate/<int:activity_id>', views.activityupdate, name='activityupdate'),
    path('portfolio/activitydelete/<int:activity_id>', views.activitydelete, name='activitydelete'),
    path('myscrap/', info.views.my_scrap, name="myscrap")
]
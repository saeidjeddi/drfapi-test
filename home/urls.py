from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
	path('', views.Home.as_view(), name='home'),
path('questions/<int:pk>/', views.QuestionsView.as_view(), name='questions_pk'),
	path('questions/', views.QuestionsView.as_view(), name='questions'),

]

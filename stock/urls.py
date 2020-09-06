from django.urls import path
# from .views import HomeView
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('api/chart/data/', views.StockData.as_view()),
	# path('chart_view/', views.StockData.as_view())
]
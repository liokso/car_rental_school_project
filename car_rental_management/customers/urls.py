from django.urls import path
from . import views
from . import *

from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'customers'

urlpatterns = [
	path('car_info', CarInfoView.as_view(), name='car_info'),
	path('', views.car_info, name='search'),
	#path('BMW', views.car_info(), name='BMW'),
	#path('search', views.search, name='search')
	path('car_list', views.CarView.as_view(), name='index'),

	path('car_list/<int:pk>/', views.DetailView.as_view(), name='detail'),
]

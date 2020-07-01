from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'employees'
urlpatterns = [
	path('', views.login, name = 'login'),
	path('main', views.main, name = 'main'),
	path('mis', views.mis, name = 'mis'),
	path('emp_man', views.employee_management, name = 'emp_man'),
	path('order_info', views.order_info, name = 'order_info'),
	path('store_info', views.store_info, name = 'store_info'),
	path('cus_info', views.customer_info, name = 'cus_info'),
	path('car_info', views.car_info, name = 'car_info'),
	path('register', views.register, name='register'),
	path('search_result', views.search_result, name='search_result'),
	path('logout', views.logout, name='logout'),
	path('profile', views.profile, name='profile'),
	path('update_profile', views.update_profile, name='update_profile'),

	path('ajax_test', views.ajax_test, name='ajax_test'),
	path('ajax/validate_conditoin', views.validate_conditoin, name='validate_conditoin')
]
from django.urls import path, re_path
from . import views
from employees.views import *
from django.contrib.auth import views as auth_views
app_name = 'employees'
urlpatterns = [
	#path('', views.login, name = 'login'),
	path('', LoginView.as_view(), name = 'login'),
	#path('main', views.main, name = 'main'),
	path('main', MainView.as_view(), name="main_view"),
	path('emp_man', HRManageView.as_view(), name = 'emp_man'),
	path('order_info', OrderInfoView.as_view(), name = 'order_info'),
	#path('order_info', views.order_info, name = 'order_info'),
	path('store_info', StoreInfoView.as_view(), name = 'store_info'),
	path('cus_info', CustomerInfoView.as_view(), name = 'cus_info'),
	path('car_info', CarInfoView.as_view(), name = 'car_info'),
	path('register', RegisterView.as_view(), name='register'),
	path('profile', ProfileView.as_view(), name='profile'),
	path('update_profile', UpdateProfileView.as_view(), name='update_profile'),
	path('mis', MISView.as_view(), name='mis'),
	path('email', VerificationView.as_view(), name='email'),
	# re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),

	#path('activate/<uidb64>/<token>', activate, name='activate'),
	path('activate/<uidb64>/<token>', ActivateView.as_view(), name='activate'),
	path('send_email', SendEmailView.as_view(), name='send_email'),
	path('update_email', UpdateEmailView.as_view(), name='update_email'),
	#path('activate/<uidb64:[0-9A-Za-z_\-]+>/<token:[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}>', views.activate, name='activate'),
	#path('mis', views.mis, name = 'mis'),

	#path('register', views.register, name='register'),
	
#	path('search_result', views.search_result, name='search_result'),
	path('search_result', SearchResultView.as_view(), name='search_result'),
	
	path('logout', auth_views.LogoutView.as_view(), name='logout'),
	#path('profile', views.profile, name='profile'),
	#path('update_profile', views.update_profile, name='update_profile'),
]
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from .controller.DBHelper import *
from .controller.Search import *
from .utils.html_data_helper import *
from django.http import HttpResponse, JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Search functions has been created in DBHelper.py

#
# logic of Main page
#

def has_logged_in(func):
	def wrapper(request, *args, **kv):
		user_info = request.session.get('is_login', None)
		if user_info:
			return redirect_to_other_pages(redirect_address['main'])
		return func(request, *args, **kv)
	return wrapper

def check_session(func):
	def wrapper(request, *args, **kv):
		user_info = request.session.get('is_login', None)
		if not user_info:
			return redirect_to_other_pages(redirect_address['root'])
		return func(request, *args, **kv)
	return wrapper

@check_session
def main(request):
	return render(request, html_addresses['main'], url_data)

#
#	A general search result page
#
@check_session
def search_result(request):
	return search_main(html_addresses['search'], GeneralSearchForm, 
		generalQuery, request, 'general')

@check_session
def car_info(request):
	return search_main(html_addresses['car_information'], CarInformationForm, 
		carInformationQuery, request, 'car_information')

@check_session
def order_info(request):	
	return search_main(html_addresses['order_information'], OrderInformationForm, 
		orderInformationQuery, request, 'order_information')

@check_session
def store_info(request):	
	return search_main(html_addresses['store_information'], StoreInformationForm, 
		storeInformationQuery, request, 'store_information')

@check_session
def customer_info(request):
	return search_main(html_addresses['customer_information'], CustomerInformationForm, 
		customerInformationSearch, request, 'customer_information')

# =======
# <<<<<<< HEAD
# def store_info(request):
	# get_current_user_level(request)
	# global search_condition
	# if request.method == 'POST':
		# form = StoreInformationForm(request.POST)
		# if form.is_valid():
			# search_condition = form.cleaned_data['search_condition']
			# search_result = storeInformationSearch(search_condition, url_data['currentUserAccessLevel'], request)
			# url_data['empty'] = 0
			# result_data = {**url_data, **search_result}
			# return render(request, html_addresses['store_information'], result_data)
		# url_data['empty'] = 1
		# return render(request, html_addresses['store_information'], url_data)
	# else:
		# search_result = storeInformationSearch(search_condition, url_data['currentUserAccessLevel'], request)
		# result_data = {**url_data, **search_result}
		# return render(request, html_addresses['store_information'], result_data)
# @login_required(login_url='/employees/')
# =======
	
# >>>>>>> 2c0f64d652593042fd493214fd703af06aa9733b
# def customer_info(request):
	# get_current_user_level(request)
	# global search_condition
	# if request.method == 'POST':
		# form = CustomerInformationForm(request.POST)
		# if form.is_valid():
			# search_condition = form.cleaned_data['search_condition']
			# search_result = customerInformationSearch(search_condition, url_data['currentUserAccessLevel'], request)
			# url_data['empty'] = 0
			# result_data = {**url_data, **search_result}
			# return render(request, html_addresses['customer_information'], result_data)
		# url_data['empty'] = 1
		# return render(request, html_addresses['customer_information'], url_data)
	# else:
		# search_result = customerInformationSearch(search_condition, url_data['currentUserAccessLevel'], request)
		# result_data = {**url_data, **search_result}
		# return render(request, html_addresses['customer_information'], result_data)
@check_session
def employee_management(request):
	return search_main(html_addresses['employee_management'], EmployeeInformationForm, 
		employeeInformationQuery, request, 'employee_management')

@check_session
def mis(request):
	global url_data
	url_data['misResult'] = ""
	
	if request.method == 'POST':
		# cityForm = CitiesSelection(request.POST)
		# if cityForm.is_valid():
			# cond3= form.cleaned_data['selectCity']
	
	
		form = MISForm(request.POST)
		if form.is_valid():
			cond1= form.cleaned_data['predOptions']
			cond2= form.cleaned_data['periodTime']
			cond3= form.cleaned_data['selectCity'][0].mis_cityID
			
			url_data['misCond1'] = cond1
			url_data['misCond2'] = cond2
			
			if cond1 and cond2 and cond3:
				misResult = MISquery(int(cond1),int(cond2), int(cond3))
				url_data['misResult'] = misResult
				#return HttpResponse(cond1)
			else:
				url_data['warning_message'] = "No data"
		else:
			url_data['warning_message'] = "No data"
	url_data['cityList'] = V_Cities.objects.all()	
	return render(request, html_addresses['mis'], url_data)

@check_session
def register(request):
	#get_current_user_level(request)
	# return HttpResponse(url_data['username'])
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			namefilter = Employee.objects.filter(employeeusername=username)
			if len(namefilter) > 0:
				return render(request, html_addresses['register'], {'form': form, 'error': 'Username has been registered', 'currentUserAccessLevel': url_data['currentUserAccessLevel'], 'username': url_data['username']}, url_data)
			else:
				passwordfirst = form.cleaned_data['passwordSet']
				passwordsecond = form.cleaned_data['passwordEnsure']
				if passwordfirst != passwordsecond:
					return render(request, html_addresses['register'], {'form': form, 'error': 'The passwords are inconsistent', 'currentUserAccessLevel': url_data['currentUserAccessLevel'], 'username': url_data['username']}, url_data)
				else:
					new_roleid = form.cleaned_data['roleID']
					email = form.cleaned_data['email']
					firstname = form.cleaned_data['firstName']
					lastname = form.cleaned_data['lastName']
					phonenumber = form.cleaned_data['phoneNumber']
					city = form.cleaned_data['city']
					address = form.cleaned_data['address']
					dob = form.cleaned_data['DOB']
					cityid = Citylist.objects.get(cityid=city)
					roleObject = Employeerole.objects.get(roleid = new_roleid)
					employee = Employee.objects.create(employeeusername=username, employeepassword=passwordfirst, roleid=roleObject,
					                                   employeeemail=email, employeefirstname=firstname, employeelastname=lastname,
					                                   employeephonenumber=phonenumber, employeecityid=cityid,
					                                   employeeaddress=address, employeedob=dob)
					employee.save()
					return redirect_to_other_pages(redirect_address['human_resource'])

	else:
		#get_current_user_level(request)
		form = SignUpForm()
	return render(request, html_addresses['register'], {'form': form, 'currentUserAccessLevel': url_data['currentUserAccessLevel'], 'username': url_data['username']})

	
def redirect_to_other_pages(redirect_address, info = ''):
	global url_data
	url_data['warning_message'] = info
	return redirect(redirect_address)

# def get_current_user_level(request):
	# current_user_set = request.user
	# employee = Employee.objects.get(employeeusername=current_user_set.username)
	# url_data['currentUserAccessLevel'] = employee.roleid.roleaccesslevel
	# url_data['username'] = employee.employeefirstname + ' ' + employee.employeelastname

@has_logged_in
def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			namefilter = Employee.objects.filter(employeeusername=username, employeepassword=password)
			if len(namefilter) > 0:
				employee = Employee.objects.get(employeeusername=username)
				request.session['is_login'] = True
				request.session['user_access_level'] = employee.roleid.roleaccesslevel
				request.session['username'] = employee.employeeusername
				request.session['name'] = employee.employeefirstname + ' ' + employee.employeelastname
				url_data['currentUserAccessLevel'] = employee.roleid.roleaccesslevel
				url_data['username'] = employee.employeefirstname + ' ' + employee.employeelastname
				return redirect_to_other_pages(redirect_address['main'])
			else:
				return render(request, html_addresses['login'], {'form': form, 'error': 'Please check your username and password'})
		else:
			return render(request, html_addresses['login'], {'form': form, 'error': 'Please check your username and password'})
	else:
		form = LoginForm()
	return render(request, html_addresses['login'], {'form': form})

def logout(request):
	if not request.session.get('is_login', None):
		return redirect_to_other_pages(redirect_address['root'])
	del request.session['is_login']
	del request.session['user_access_level']
	del request.session['username']
	del request.session['name']
	return redirect_to_other_pages(redirect_address['root'])


@check_session
def profile(request):
	current_user_set = request.session['username']
	employee = Employee.objects.get(employeeusername=current_user_set)
	return render(request, html_addresses['profile'], {'employee': employee,
	                                                   'currentUserAccessLevel': url_data['currentUserAccessLevel'], 'username': url_data['username']})

@check_session
def update_profile(request):
	
	current_user_set = request.session['username']
	employee = Employee.objects.get(employeeusername=current_user_set)

	if request.method == 'POST':
		form = UpdateProfileForm(request.POST)
		if form.is_valid():
			employee.employeeemail = form.cleaned_data['email']
			employee.employeefirstname = form.cleaned_data['firstName']
			employee.employeelastname = form.cleaned_data['lastName']
			employee.employeephonenumber = form.cleaned_data['phoneNumber']
			employee.employeecityid = Citylist.objects.get(cityid=int(form.cleaned_data['city']))
			employee.employeeaddress = form.cleaned_data['address']
			employee.save()
			global url_data
			url_data['username'] = employee.employeefirstname + " " + employee.employeelastname
			return redirect_to_other_pages(redirect_address['profile'])
		else:
			return render(request, html_addresses['update_profile'], {'form': form, 'error': 'Update fail', 'currentUserAccessLevel': url_data['currentUserAccessLevel'], 'username': url_data['username']})
	else:
		default_data = {'email': employee.employeeemail, 'firstName': employee.employeefirstname, 'lastName': employee.employeelastname,
		                'phoneNumber': employee.employeephonenumber, 'city': employee.employeecityid.cityid,
		                'address': employee.employeeaddress}
		form = UpdateProfileForm(default_data)
		return render(request, html_addresses['update_profile'], {'form': form, 'currentUserAccessLevel': url_data['currentUserAccessLevel'], 'username': url_data['username']})
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#
# These code below just for test
def ajax_test(request):
	return render(request, 'employees/ajax_test.html')
	
def validate_conditoin(request):
	username = request.GET.get('username')
	data = {
		'is_taken': username + 'Hello'
	}
	#search_result = generySearch(username, 5, request)
	#search_result['employees'].object_list
	return HttpResponse(search_result['employees'].object_list[0].employeefirstname)


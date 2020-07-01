from .base_views import *

from django.core.files import File
import os

from .utils.html_data_helper import *
from django.http import HttpResponse

import math


from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .token import account_activation_token

# Search functions has been created in DBHelper.py


#
# logic of Main View
#
class MainView(BaseView):

	address = html_addresses['main']
	mainController = MainController()
	
	def pre_get(self, request):
		car_remaining = self.mainController.get_car_remaining()
		active_store = self.mainController.get_active_store()
		recent_order = self.mainController.get_recent_order()
		new_customer = self.mainController.get_new_customer()
		
		self.result_data = {'car_remaining': car_remaining, 
							'active_store': active_store,
							'recent_order': recent_order,
							'new_customer': new_customer}

#
# Car Information View
#
class CarInfoView(AdvanceSearchResultView):
	carController = CarInfoController()
	address = html_addresses['car_information']
	
	def pre_get(self, request):
		# self.reload_general_search_result(carInformationQuery, request, 'car_information')
		if url_search_condition['car_information_advance'] == '':
			# self.result_data = self.carController.general_search(url_search_condition['car_information'], request, carInformationQuery)
			sorting_condition = request.session['car_information']
			self.result_data = self.carController.order_gernal_search_result(url_search_condition['car_information'], request, sorting_condition)
		else:
			# self.result_data = self.carController.reload_advance_data(url_search_condition['car_information_advance'], request, carInformationQuery)
			sorting_condition = request.session['car_information_advance']
			self.result_data = self.carController.order_advance_search_result(url_search_condition['car_information_advance'], sorting_condition, request)

		
	# def post(self, request, *args, **kwargs):
	def pre_post(self, request):
		#self.general_search(CarInformationForm, carInformationQuery, request, 'car_information')
		form = CarInformationForm(request.POST)
		if "advance_search" in request.POST:
			if form.is_valid():				
				search_result = self.query_advance_conditoin_result(form, self.carController.car_advance_search, url_search_condition, request)
				self.result_data = search_result
			else:
				self.result_data = {"msg": "Form input is not correct."}
		elif "btn_order" in request.POST:
			if form.is_valid():
				self.result_data = self.carController.order_result(form, 'car_information', 'car_information_advance',
						self.carController.order_gernal_search_result, self.carController.order_advance_search_result, url_search_condition, request)
		else:
			if form.is_valid():
				url_search_condition['car_information'] = form.cleaned_data['search_condition']
			else:
				url_search_condition['car_information'] = ''
				
			url_search_condition['car_information_advance'] = ''
			self.result_data = self.carController.general_search(url_search_condition['car_information'], request, carInformationQuery)
		
		#return HttpResponse(str(self.result_data))


#
# Order Information View
#	processing the logic of Order Information web page actions
#
class OrderInfoView(DateAdvanceSearchResultView):
	orderInfoController = OrderInfoController()
	
	address = html_addresses['order_information']
	
	def get_date_query_sentence(self, form):
		start_date_create = form.cleaned_data['start_date_create']
		end_date_create = form.cleaned_data['end_date_create']
		start_date_pick = form.cleaned_data['start_date_pick']
		end_date_pick = form.cleaned_data['end_date_pick']
		start_date_return = form.cleaned_data['start_date_return']
		end_date_return = form.cleaned_data['end_date_return']
		
		date_query_sentence = ""
		date_query_sentence = self.create_date_query_sentence(date_query_sentence, "createDate", start_date_create, True)
		date_query_sentence = self.create_date_query_sentence(date_query_sentence, "createDate", end_date_create, False)
		date_query_sentence = self.create_date_query_sentence(date_query_sentence, "pickupDate", start_date_pick, True)
		date_query_sentence = self.create_date_query_sentence(date_query_sentence, "pickupDate", end_date_pick, False)
		date_query_sentence = self.create_date_query_sentence(date_query_sentence, "returnDate", start_date_return, True)
		date_query_sentence = self.create_date_query_sentence(date_query_sentence, "returnDate", end_date_return, False)
				
		return date_query_sentence
	
	def pre_get(self, request):
		#self.reload_general_search_result(orderInformationQuery, request, 'order_information')
		if url_search_condition['order_information_advance'] == '':
			# self.result_data = self.orderInfoController.general_search(url_search_condition['order_information'], request, orderInformationQuery)
			sorting_condition = request.session['order_information']
			self.result_data = self.orderInfoController.order_gernal_search_result(url_search_condition['order_information'], request, sorting_condition)
		else:
			# self.result_data = self.orderInfoController.reload_advance_data(url_search_condition['order_information_advance'], request, orderInformationQuery)
			sorting_condition = request.session['order_information_advance']
			self.result_data = self.orderInfoController.order_advance_search_result(url_search_condition['order_information_advance'], sorting_condition, request)
		
	def pre_post(self, request):
		# self.general_search(OrderInformationForm, orderInformationQuery, request, 'order_information')
		form = OrderInformationForm(request.POST)
		
		if "advance_search" in request.POST:
			if form.is_valid():
				search_result = self.query_advance_conditoin_result(form, self.orderInfoController.order_advance_search, url_search_condition, request)
				self.result_data = search_result
			else:
				self.result_data = {"msg": "Form input is not correct."}
				
		elif "btn_order" in request.POST:
			if form.is_valid():
				self.result_data = self.orderInfoController.order_result(form, 'order_information', 'order_information_advance',
						self.orderInfoController.order_gernal_search_result, self.orderInfoController.order_advance_search_result, url_search_condition, request)
		else:
			if form.is_valid():
				url_search_condition['order_information'] = form.cleaned_data['search_condition']
			else:
				url_search_condition['order_information'] = ''
				
			url_search_condition['order_information_advance'] = ''
			
			self.result_data = self.orderInfoController.general_search(url_search_condition['order_information'], request, orderInformationQuery)
	

#
# Store Information View
#
class StoreInfoView(AdvanceSearchResultView):
	storeInfoController = StoreInfoController()
	
	address = html_addresses['store_information']
	
	def pre_get(self, request):
		if url_search_condition['store_information_advance'] == '':
			# self.result_data = self.storeInfoController.general_search(url_search_condition['store_information'], request, storeInformationQuery)
			sorting_condition = request.session['store_information']
			self.result_data = self.storeInfoController.order_gernal_search_result(url_search_condition['store_information'], request, sorting_condition)
		else:
			# self.result_data = self.storeInfoController.reload_advance_data(url_search_condition['store_information_advance'], request, storeInformationQuery)
			sorting_condition = request.session['store_information_advance']
			self.result_data = self.storeInfoController.order_advance_search_result(url_search_condition['store_information_advance'], sorting_condition, request)
		
	def pre_post(self, request):
	#def post(self, request, *args, **kwargs):
		form = StoreInformationForm(request.POST)
		
		if "advance_search" in request.POST:
			if form.is_valid():
				search_result = self.query_advance_conditoin_result(form, self.storeInfoController.store_advance_search, url_search_condition, request)
				self.result_data = search_result
			else:
				self.result_data = {"msg": "Form input is not correct."}
				
		elif "btn_order" in request.POST:
			if form.is_valid():
				self.result_data = self.storeInfoController.order_result(form, 'store_information', 'store_information_advance',
						self.storeInfoController.order_gernal_search_result, self.storeInfoController.order_advance_search_result, url_search_condition, request)
		else:
			if form.is_valid():
				url_search_condition['store_information'] = form.cleaned_data['search_condition']
			else:
				url_search_condition['store_information'] = ''
				#return HttpResponse(str(form))
				
			url_search_condition['store_information_advance'] = ''
			self.result_data = self.storeInfoController.general_search(url_search_condition['store_information'], request, storeInformationQuery)
	

#
# Customer Information View
#
#
class CustomerInfoView(DateAdvanceSearchResultView):
	customerInfoController = CustomerInfoController()
	
	address = html_addresses['customer_information']
	
	#
	# Get date query sentence
	#
	# return: the date query sentence
	def get_date_query_sentence(self, form):
		start_date = form.cleaned_data['start_date']
		end_date = form.cleaned_data['end_date']
		
		date_query_sentence = ""
		
		date_query_sentence = self.create_date_query_sentence(date_query_sentence, "customerDOB", start_date, True)
		date_query_sentence = self.create_date_query_sentence(date_query_sentence, "customerDOB", end_date, False)
		
		return date_query_sentence
		
	
	def pre_get(self, request):
		# sorting_condition = request.session['customer_information']
		#import pdb; pdb.set_trace()
		if url_search_condition['customer_information_advance'] == '':
			# self.result_data = self.customerInfoController.general_search(url_search_condition['customer_information'], request, customerInformationSearch)
			# order_gernal_search_result
			sorting_condition = request.session['customer_information']
			self.result_data = self.customerInfoController.order_gernal_search_result(url_search_condition['customer_information'], request, sorting_condition)
		else:
			# self.result_data = self.customerInfoController.reload_advance_data(url_search_condition['customer_information_advance'], request, customerInformationSearch)
			# order_advance_search_result
			sorting_condition = request.session['customer_information_advance']
			self.result_data = self.customerInfoController.order_advance_search_result(url_search_condition['customer_information_advance'], sorting_condition, request)
			
	def pre_post(self, request):
		form = CustomerInformationForm(request.POST)
		if "advance_search" in request.POST:
			if form.is_valid():				
				search_result = self.query_advance_conditoin_result(form, self.customerInfoController.customer_advance_search, url_search_condition, request)
				self.result_data = search_result
			else:
				self.result_data = {"msg": "Form input is not correct."}
		elif "btn_order" in request.POST:
			if form.is_valid():
				self.result_data = self.customerInfoController.order_result(form, 'customer_information', 'customer_information_advance',
						self.customerInfoController.order_gernal_search_result, self.customerInfoController.order_advance_search_result, url_search_condition, request)
		else:
			if form.is_valid():
				url_search_condition['customer_information'] = form.cleaned_data['search_condition']
			else:
				url_search_condition['customer_information'] = ''
				
			url_search_condition['customer_information_advance'] = ''
			self.result_data = self.customerInfoController.general_search(url_search_condition['customer_information'], request, customerInformationSearch)

#
# Human Resource Management View
#
class HRManageView(DateAdvanceSearchResultView):
	hrManageController = HRManageController() 
	
	address = html_addresses['employee_management']
		
	def get_date_query_sentence(self, form):
		start_date = form.cleaned_data['start_date']
		end_date = form.cleaned_data['end_date']
		
		date_query_sentence = ""
		date_query_sentence = self.create_date_query_sentence(date_query_sentence, "employeeDOB", start_date, True)
		date_query_sentence = self.create_date_query_sentence(date_query_sentence, "employeeDOB", end_date, False)
		
		return date_query_sentence
	
	def pre_get(self, request):
		if url_search_condition['employee_management_advance'] == '':
			# self.result_data = self.hrManageController.general_search(url_search_condition['employee_management'], request, employeeInformationQuery)
			sorting_condition = request.session['employee_management']
			self.result_data = self.hrManageController.order_gernal_search_result(url_search_condition['employee_management'], request, sorting_condition)
		else:
			# self.result_data = self.hrManageController.reload_advance_data(url_search_condition['employee_management_advance'], request, employeeInformationQuery)
			sorting_condition = request.session['employee_management_advance']
			self.result_data = self.hrManageController.order_advance_search_result(url_search_condition['employee_management_advance'], sorting_condition, request)
		
	def pre_post(self, request):
		
		form = EmployeeInformationForm(request.POST)
		
		if "advance_search" in request.POST:
			if form.is_valid():				
				search_result = self.query_advance_conditoin_result(form, self.hrManageController.hr_advance_search, url_search_condition, request)
				self.result_data = search_result
			else:
				self.result_data = {"msg": "Form input is not correct."}
		elif "btn_order" in request.POST:
			if form.is_valid():
				self.result_data = self.hrManageController.order_result(form, 'employee_management', 'employee_management_advance',
						self.hrManageController.order_gernal_search_result, self.hrManageController.order_advance_search_result, url_search_condition, request)
		else:
			if form.is_valid():
				url_search_condition['employee_management'] = form.cleaned_data['search_condition']
			else:
				url_search_condition['employee_management'] = ''
				
			url_search_condition['employee_management_advance'] = ''
			self.result_data = self.hrManageController.general_search(url_search_condition['employee_management'], request, employeeInformationQuery)

#
# Register View
#
class RegisterView(BaseView):
	registerController = RegisterController()
	
	def get(self, request, *args, **kwargs):
		#self.pre_get(request)
		form = SignUpForm()
		return render(request, html_addresses['register'], {'form': form})
		#return render(request, self.address, self.result_data)	
	
	def post(self, request, *args, **kwargs):
		form = SignUpForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			if self.registerController.checkIfUserExist(username):
				return render(request, html_addresses['register'], {'form': form, 'error': 'Username has been registered'})
			else:
				passwordfirst = form.cleaned_data['passwordSet']
				passwordsecond = form.cleaned_data['passwordEnsure']
				if passwordfirst != passwordsecond:
					return render(request, html_addresses['register'], {'form': form, 'error': 'The passwords are inconsistent'})
				else:
					new_roleid = form.cleaned_data['roleID']
					email = form.cleaned_data['email']
					firstname = form.cleaned_data['firstName']
					lastname = form.cleaned_data['lastName']
					phonenumber = form.cleaned_data['phoneNumber']
					city = form.cleaned_data['city']
					address = form.cleaned_data['address']
					dob = form.cleaned_data['DOB']
					self.registerController.save_new_employee(city, new_roleid, username,
									passwordfirst, email, firstname, lastname, phonenumber,
									address, dob)
					return redirect(redirect_address['human_resource'])


#
# Login
#
class LoginView(View):
	loginController = LoginController()
	 
	#
	# Check if user has logined into the system
	#
	def dispatch(self, request, *args, **kwargs):
		user_info = request.session.get('is_login', None)
		if user_info:
			return redirect(redirect_address['main'])
		return super().dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		form = LoginForm()
		return render(request, html_addresses['login'], {'form': form})
		
	def post(self, request, *args, **kwargs):
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			if self.loginController.checkIfUserExist(username):

				if self.loginController.checkIfUserBan(username):
					return render(request, html_addresses['login'],
					              {'form': form,
					               'error': 'This use has been banned, Please contact with IT support team'})

				if self.loginController.checkIfUserExist(username, password):
					self.loginController.changeSessionState(request, username)
					employee = Employee.objects.get(employeeusername=username)
					employee.employeeloginattempt = 0
					employee.save()
					return redirect(redirect_address['main'])
				else:
					attemptlimit = 5
					employee = Employee.objects.get(employeeusername=username)
					employee.employeeloginattempt += 1
					employee.save()
					restattempt = attemptlimit - employee.employeeloginattempt
					return render(request, html_addresses['login'], {'form': form,
					                                                 'error': 'Please check your password, your rest attempt chance: ' + str(
						                                                 restattempt)})
			else:
				return render(request, html_addresses['login'],
				              {'form': form, 'error': 'Please check your username'})
		else:
			return render(request, html_addresses['login'], {'form': form, 'error': 'Please check your form'})


#
# Show Profile
#
class ProfileView(BaseView):
	profileController = ProfileController()
	address = html_addresses['profile']
	
	def pre_get(self, request):
		current_user_name= request.session['username']
		employee = self.profileController.get_current_user(current_user_name)
		self.result_data = {'employee': employee}

#
# Update Profile
#
class UpdateProfileView(BaseView):
	updateProfileController = UpdateProfileController()
	
	def get(self, request, *args, **kwargs):
		default_data = self.updateProfileController.get_user_information(request.session['username'])
		form = UpdateProfileForm(default_data)
		return render(request, html_addresses['update_profile'], {'form': form})
		
	def post(self, request, *args, **kwargs):
		form = UpdateProfileForm(request.POST)
		if form.is_valid():
			self.updateProfileController.updateUserProfile(request.session['username'],
				form.cleaned_data['email'],
				form.cleaned_data['firstName'],
				form.cleaned_data['lastName'],
				form.cleaned_data['phoneNumber'],
				form.cleaned_data['city'],
				form.cleaned_data['address'], request)
			return redirect(redirect_address['profile'])
		else:
			return render(request, html_addresses['update_profile'], {'form': form, 'error': 'Update fail'})
	
class VerificationView(BaseView):
	emailController = EmailController()

	def get(self, request, *args, **kwargs):
		username = request.session['username']
		currentEmployee = self.emailController.get_current_user(username)
		form = EmailVerification()
		success_info = self.emailController.message_generate(currentEmployee, form, request)
		if success_info != 'Null':
			return render(request, html_addresses['email'], {'user': currentEmployee, 'form': form,
			                                                 'success_info': success_info})
		else:
			return render(request, html_addresses['email'], {'user': currentEmployee, 'form': form})

	def post(self, request, *args, **kwargs):
		form = EmailVerification(request.POST)
		username = request.session['username']
		currentEmployee = self.emailController.get_current_user(username)
		if form.is_valid():
			if currentEmployee.employeeemail != form.cleaned_data['email']:
				return render(request, html_addresses['email'], {'user': currentEmployee, 'form': form,
				                                                 'error': 'Input email not match your register email'})
			self.emailController.send_verification_email(request, currentEmployee)
			return redirect(redirect_address['email'])

class ActivateView(View):
	def get(self, request, *args, **kwargs):
		try:
			uid = urlsafe_base64_decode(kwargs['uidb64']).decode()
			user = Employee.objects.get(pk=uid)
		except(TypeError, ValueError, OverflowError, Employee.DoesNotExist):
			user = None
		if user is not None and account_activation_token.check_token(user, kwargs['token']):
			user.employeeemailverify = '1'
			user.save()
			return HttpResponse('Thank you for your email confirmation. Now you can use email function.')
		else:
			return HttpResponse('Activation link is invalid!')

class SendEmailView(BaseView):
	emailController = EmailController()

	def get(self, request, *args, **kwargs):
		username = request.session['username']
		currentEmployee = self.emailController.get_current_user(username)
		form = SendEmailForm()
		userChoice = self.emailController.generate_user_list()

		return render(request, html_addresses['send_email'],
		              {'user': currentEmployee, 'form': form, 'userChoice': userChoice})

	def post(self, request, *args, **kwargs):
		username = request.session['username']
		currentEmployee = self.emailController.get_current_user(username)
		form = SendEmailForm(request.POST)
		userChoice = self.emailController.generate_user_list()

		if form.is_valid():
			username = request.session['username']
			currentEmployee = self.emailController.get_current_user(username)
			check_box_list = request.POST.getlist('userBox')

			if len(check_box_list) == 0:
				error = 'Please choose email receiver'
				return render(request, html_addresses['send_email'], {'user': currentEmployee, 'form': form, 'userChoice': userChoice, 'error': error})

			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			self.emailController.send_email(message, currentEmployee, subject, check_box_list, request)

			return redirect(redirect_address['email'])
		else:
			return HttpResponse('Send email fail')


class UpdateEmailView(BaseView):
	emailController = EmailController()

	def get(self, request, *args, **kwargs):
		username = request.session['username']
		currentEmployee = self.emailController.get_current_user(username)
		default_data = {'email': currentEmployee.employeeemail}
		form = UpdateEmailForm(default_data)
		return render(request, html_addresses['update_email'], {'user': currentEmployee, 'form': form})

	def post(self, request, *args, **kwargs):
		form = UpdateEmailForm(request.POST)
		username = request.session['username']
		currentEmployee = self.emailController.get_current_user(username)

		if form.is_valid():
			new_email = form.cleaned_data['email']
			error = self.emailController.check_email(new_email, currentEmployee)

			if error != 'Null':
				default_data = {'email': currentEmployee.employeeemail}
				form = UpdateEmailForm(default_data)
				return render(request, html_addresses['update_email'],
			              {'user': currentEmployee, 'form': form, 'error': error})

			else:
				self.emailController.update_email(new_email, currentEmployee, request)
				return redirect(redirect_address['email'])


class MISView(BaseView):
	url_data['misResult'] = ""
	address = html_addresses['mis']
	misController = MISController()
	
	def pre_post(self, request):
		form = MISForm(request.POST)
		if form.is_valid():
		
			cond1 = form.cleaned_data['predOptions']
			cond2 = form.cleaned_data['periodTime']
			cond2a = form.cleaned_data['numberOf']
			cond3 = form.cleaned_data['selectCity']
			cond3all = form.cleaned_data['allCities']
			url_data['misCond1'] = cond1
			url_data['misCond2'] = cond2
			url_data['misCond2a'] = cond2a
			url_data['misCond3all'] = cond3all
			
			if cond3:
				cond3 = form.cleaned_data['selectCity'][0].mis_cityID
				cond3name = form.cleaned_data['selectCity'][0].mis_cityName
				url_data['misCond3'] = cond3
			else:
				cond3 = "0"
					
			cond4 = form.cleaned_data['vWheelDrive']
			cond4a = form.cleaned_data['wheelDrive']
			cond5 = form.cleaned_data['vNoSeats']
			cond5a = form.cleaned_data['optNS1']
			cond5b = form.cleaned_data['optNS2']
			cond6 = form.cleaned_data['vTankCapacity']
			cond6a = form.cleaned_data['optTC1']
			cond6b = form.cleaned_data['optTC2']
			cond7 = form.cleaned_data['vPower']
			cond7a = form.cleaned_data['optPW1']
			cond7b = form.cleaned_data['optPW2']
			cond8 = form.cleaned_data['vEngineSize']
			cond8a = form.cleaned_data['optES1']
			cond8b = form.cleaned_data['optES2']
			cond9 = form.cleaned_data['vCarYear']
			cond9a = form.cleaned_data['optCY1']
			cond9b = form.cleaned_data['optCY2']			
			cond10 = form.cleaned_data['vWheelBase']
			cond10a = form.cleaned_data['optWB1']
			cond10b = form.cleaned_data['optWB2']
			cond11 = form.cleaned_data['vTransmission']
			cond11a = form.cleaned_data['transmission']
			cond12 = form.cleaned_data['selectMakeModel']
			
			url_data['misCond4'] = cond4
			url_data['misCond4a'] = cond4a
			url_data['misCond5'] = cond5
			url_data['misCond5a'] = cond5a
			url_data['misCond5b'] = cond5b
			url_data['misCond6'] = cond6
			url_data['misCond6a'] = cond6a
			url_data['misCond6b'] = cond6b
			url_data['misCond7'] = cond7
			url_data['misCond7a'] = cond7a
			url_data['misCond7b'] = cond7b
			url_data['misCond8'] = cond8
			url_data['misCond8a'] = cond8a
			url_data['misCond8b'] = cond8b
			url_data['misCond9'] = cond9
			url_data['misCond9a'] = cond9a
			url_data['misCond9b'] = cond9b
			url_data['misCond10'] = cond10
			url_data['misCond10a'] = cond10a
			url_data['misCond10b'] = cond10b
			url_data['misCond11'] = cond11
			url_data['misCond11a'] = cond11a
			url_data['misCond12'] = cond12
			
			cond12a = form.cleaned_data['selectMake']
			cond12b = form.cleaned_data['selectModel']
			if cond12a:
				cond12c = form.cleaned_data['selectMake'][0].mis_makeName
				url_data['misCond12c'] = form.cleaned_data['selectMake'][0].mis_makeID
			elif cond12b:
				cond12c = form.cleaned_data['selectModel'][0].mis_modelName
				url_data['misCond12c'] = form.cleaned_data['selectModel'][0].mis_modelID
			
			
			yInfo = "Total"
			xInfo = "Month"
			
			analysisMessage = ['The results on the table and graph are based on the following selection:']
			
			
			if cond1 and cond2 and (cond3 or cond3all):
				
				
				sql_QuerystrAND = ""
				sql_QueryWhere = "WHERE "
				sql_QuerystrFilter = ""
				
				if cond1 == '2':
					if cond3 != '0':
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + " pickupStoreCity = '" + cond3name + "'"
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Cars Picked up from City: ' + cond3name + ';')
					else:
						analysisMessage.append('Cars Picked up considering all cities;')
					
				elif cond1 == '3':
					if cond3 != '0':
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + " returnStoreCity = '" + cond3name + "'"
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Cars Returned to City: ' + cond3name + ';')
					else:
						analysisMessage.append('Cars Returned considering all cities;')
				
				if cond2a == '2':
					sql_QuerystrCount = "COUNT(DISTINCT makeName) as NumSales FROM v_salesorder "
					
					if cond2 == '1':
						analysisMessage.append('Number of Different Makes by Month;')
					elif cond2 == '2':
						analysisMessage.append('Number of Different Makes by Quarter;')
					elif cond2 == '3':
						analysisMessage.append('Number of Different Makes by Year;')
					elif cond2 == '4':
						analysisMessage.append('Number of Different Makes by Month Over Year;')
					elif cond2 == '5':
						analysisMessage.append('Number of Different Makes by Quarter Over Year;')
					elif cond2 == '6':
						analysisMessage.append('Top 10 Cities with highest number of Different Makes;')
					
				elif cond2a == '3':
					sql_QuerystrCount = "COUNT(DISTINCT model) as NumSales FROM v_salesorder "
					if cond2 == '1':
						analysisMessage.append('Number of Different Models by Month;')
					elif cond2 == '2':
						analysisMessage.append('Number of Different Models by Quarter;')
					elif cond2 == '3':
						analysisMessage.append('Number of Different Models by Year;')
					elif cond2 == '4':
						analysisMessage.append('Number of Different Models by Month Over Year;')
					elif cond2 == '5':
						analysisMessage.append('Number of Different Models by Quarter Over Year;')
					elif cond2 == '6':
						analysisMessage.append('Top 10 Cities with highest number of Different Models;')
				else:
					sql_QuerystrCount = "COUNT(orderID) as NumSales FROM v_salesorder "		
					if cond2 == '1':
						analysisMessage.append('Number of Sales by Month;')
					elif cond2 == '2':
						analysisMessage.append('Number of Sales by Quarter;')
					elif cond2 == '3':
						analysisMessage.append('Number of Sales by Year;')
					elif cond2 == '4':
						analysisMessage.append('Number of Sales by Month Over Year;')
					elif cond2 == '5':
						analysisMessage.append('Number of Sales by Quarter Over Year;')
					elif cond2 == '6':
						analysisMessage.append('Top 10 Cities with highest number of Sales;')
			
				
				if cond2 == '2':
					if cond1 == '3':
						sql_QuerystrSel = "SELECT quarter(returnDate) as salesQuarter, "
					else:
						sql_QuerystrSel = "SELECT quarter(pickupDate) as salesQuarter, "
					
					analysisMessage.append('')
					sql_QuerystrGroup = " GROUP BY salesQuarter ORDER BY salesQuarter;"
					xInfo = "Quarter"

				elif cond2 == '3':
					if cond1 == '3':
						sql_QuerystrSel = "SELECT year(returnDate) as salesYear, "
					else:
						sql_QuerystrSel = "SELECT year(pickupDate) as salesYear, "
					sql_QuerystrGroup = " GROUP BY salesYear ORDER BY salesYear;"
					xInfo = "Year"
				elif cond2 == '4':
					if cond1 == '3':
						sql_QuerystrSel = "SELECT month(returnDate) as salesMonthNum, monthname(returnDate) as salesMonth, year(returnDate) as salesYear, "
					else:
						sql_QuerystrSel = "SELECT month(pickupDate) as salesMonthNum, monthname(pickupDate) as salesMonth, year(pickupDate) as salesYear, "
					sql_QuerystrGroup = " GROUP BY salesMonth, salesYear ORDER BY salesYear, salesMonthNum;"
					xInfo = "Month Over Year"
				elif cond2 == '5':
					if cond1 == '3':
						sql_QuerystrSel = "SELECT quarter(returnDate) as salesQuarter, year(returnDate) as salesYear, "
					else:
						sql_QuerystrSel = "SELECT quarter(pickupDate) as salesQuarter, year(pickupDate) as salesYear, "
					
					sql_QuerystrGroup = " GROUP BY salesQuarter, salesYear ORDER BY salesYear, salesQuarter;"
					xInfo = "Quarter Over Year"
				elif cond2 == '6':
					if cond1 == '3':
						sql_QuerystrSel = "SELECT returnStoreCity, "
						sql_QuerystrGroup = " GROUP BY returnStoreCity ORDER BY NumSales DESC, returnStoreCity;"
						xInfo = "Top 10 Car Return City"
					else:
						sql_QuerystrSel = "SELECT pickupStoreCity, "
						sql_QuerystrGroup = " GROUP BY pickupStoreCity ORDER BY NumSales DESC, pickupStoreCity;"
						xInfo = "Top 10 Car Pickup City"

				else:
					sql_QuerystrSel = "SELECT month(pickupDate) as salesMonthNum, monthname(pickupDate) as salesMonth, "
					sql_QuerystrGroup = " GROUP BY salesMonth ORDER BY salesMonthNum; "
					xInfo = "Month"
						
				
				
				if cond4 == True:
					if cond4a == '1':
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "wheelDrive = 'FWD'"
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Wheel Drive System: FWD;')
					elif cond4a == '2':
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "wheelDrive = 'RWD'"
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Wheel Drive System: RWD;')
					else:
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "wheelDrive = '4WD'"
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Wheel Drive System: 4WD;')
						
				if cond5 == True:
					if cond5a.isnumeric():
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "seatingCapacity >= " + cond5a
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Number of Seats euqla or more than ' + cond5a + ';')
					if cond5b.isnumeric():
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "seatingCapacity <= " + cond5b
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Number of Seats equal or less than ' + cond5b + ';')
						
				if cond6 == True:
					if cond6a.isnumeric():
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "tankCapacity >= " + cond6a
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Tank Capacity with euqla or more than ' + cond6a + ';')
					if cond6b.isnumeric():
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "tankCapacity <= " + cond6b
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Tank Capacity with equal or less than ' + cond6b + ';')
						
				if cond7 == True:
					if cond7a.isnumeric():
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "power >= " + cond7a
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Engine Power euqla or higher than ' + cond7a + ';')
					if cond7b.isnumeric():
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "power <= " + cond7b
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Engine Power equal or lower than ' + cond7b + ';')
						
				if cond8 == True:
					if cond8a.isnumeric():
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "engineSize >= " + cond8a
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Engine Size with equal or more than ' + cond8a + ' litres;')
						
					if cond8b.isnumeric():
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "engineSize <= " + cond8b
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Engine Size with equal or less than ' + cond8b + ' litres;')
						
						
				if cond9 == True:
					if cond9a.isnumeric():
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "seriesYear >= " + cond9a
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Series year equal or older than ' + cond9a + ' years;')
					if cond9b.isnumeric():
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "seriesYear <= " + cond9b
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Series year equal or younger than ' + cond9b + ' years;')
						
						
				if cond10 == True:
					if cond10a.isnumeric():
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "wheelBase >= " + cond10a
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Wheel base equal or bigger than ' + cond10a + 'mm;')
					if cond10b.isnumeric():
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "wheelBase <= " + cond10b
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Wheel base equal or smaller than ' + cond10b + ' mm;')
						
				if cond11 == True:
					if cond4a == '1':
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "transmission = 'A'"
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Vehicle with Automatic Transmission;')
					else:
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "transmission = 'M'"
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Vehicle with Manual Transmission;')
						
				if cond12 == '2':
					if cond12a:
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "makeName = '" + cond12c + "'"
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Only made by make: ' + cond12c +';')
				
				elif cond12 == '3':
					if cond12b:
						sql_QuerystrFilter = sql_QuerystrFilter + sql_QueryWhere + sql_QuerystrAND + "model = '" + cond12c + "'"
						sql_QuerystrAND = " AND "
						sql_QueryWhere = ""
						analysisMessage.append('Only model: ' + cond12c +';')				
				
				
				url_data['misMessage'] = analysisMessage
				
				sql_Querystr = sql_QuerystrSel + sql_QuerystrCount + sql_QuerystrFilter + sql_QuerystrGroup
				
				
				misResult = MISquery(sql_Querystr)
				
		
				if cond2 == '1' or cond2 == '5':
					resultIndex = 2
				elif cond2 == '2' or cond2 == '3':
					resultIndex = 1
				elif cond2 == '4':
					resultIndex = 3	
				elif cond2 == '6':
					resultIndex = 1
					misResult = misResult[0:10]
				
				url_data['misResult'] = misResult
				
				maxValue = self.checkMax(misResult, resultIndex)
				minValue = self.checkMin(misResult, resultIndex)
				resultLength = len(misResult)
				if resultLength > 0:
					stepSize = math.ceil((maxValue - minValue) / resultLength)
					url_data['warning_message'] = ""
				else:
					url_data['warning_message'] = "No data"
					stepSize = 5
				
				if stepSize < 5:
					stepSize = 5
				
				if minValue - stepSize/2 < 0:
					minValue = 0
				else:
					minValue = minValue - stepSize/2
					
				url_data['maxValue'] = maxValue + stepSize
				url_data['minValue'] = minValue
				url_data['stepSize'] = stepSize
				url_data['yInfo'] = yInfo
				url_data['xInfo'] = xInfo

			else:
				url_data['warning_message'] = "No data"
		else:
			url_data['warning_message'] = "No data"
			
		#url_data['cityList'] = self.misController.get_city_objects()
		url_data['cityList'] = V_Cities.objects.all()
		url_data['makeList'] = V_VehicleMake.objects.all() 
		url_data['modelList'] = V_VehicleModel.objects.all()
		self.result_data = url_data
		
	def checkMin(self, list, index):
		minValue = 0
		for element in list:
			if element[index] < minValue:
				minValue = element[index]
				
		return minValue
	
	def checkMax(self, list, index):
		maxValue = 0
		for element in list:
			if element[index] > maxValue:
				maxValue = element[index]
		return maxValue
		
	def pre_get(self, request):
		#url_data['cityList'] = self.misController.get_city_objects()
		url_data['cityList'] = V_Cities.objects.all()
		url_data['makeList'] = V_VehicleMake.objects.all() 
		url_data['modelList'] = V_VehicleModel.objects.all()
		self.result_data = url_data
from .BaseControllers import *
from ..models import *
from .DBHelper import *


from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from employees.token import account_activation_token
from django.core.mail import EmailMessage, EmailMultiAlternatives


#
# Main Controller
# manipulate the logic of the main page
#

class MainController(BaseController):

	#
	# Return the number of remaining car
	#
	#
	# Return the number of remaining car
	#

	def get_car_remaining(self):
		return 100
	
	#
	# Return the 
	#
	def get_active_store(self):
		order_set = queryOrder('', '-pickupdate')
		if len(order_set) > 0:
			return order_set[0].pickupstoreid.storename
		return 'Data Not Found'
		
	def get_recent_order(self):
		order_set = queryOrder('', '-pickupdate')
		if len(order_set) > 0:
			return 'order id-' + str(order_set[0].orderid)
		return 'Data Not Found'
		
	def get_new_customer(self):
		order_set = queryOrder('', '-pickupdate')
		if len(order_set) > 0:
			return order_set[0].customerid.customerfirstname
		return 'Data Not Found'

#
# Search Result Controller
# manipulate the logic of the main Search Result page
#		
class SearchResultController(BaseSearchController):
	pass
	
#
# Car Controller
# manipulate the logic of the car informationi page
#	
class CarInfoController(AdvanceSearchController):
	
	#
	# Car advance search
	# 
	# condition_values: an array contains all condition values
	# condition_categories: an array indicates which column is being used
	# condition_connections: an array indicates the connection between two search conditions
	# url_search_condition: search conditionquery_advance_conditoin_result
	#
	# return: query result
	def car_advance_search(self, condition_values, condition_categories, condition_connections, request, url_search_condition, order_sentence = ""):
		query_sentence = self.compound_query_sentence(condition_values, condition_categories, condition_connections, 'vehicle')
		url_search_condition['car_information'] = ""
		url_search_condition['car_information_advance'] = query_sentence
		query_sentence += order_sentence
		self.clean_stored_sorting_condition(request)
		
		return carInformationQuery(query_sentence, request, advance = True)
		
	def order_advance_search_result(self, query_sentence, order_sentence, request):
		query_sentence += order_sentence
		return carInformationQuery(query_sentence, request, advance = True)
		
	def order_gernal_search_result(self, condition, request, orderCondition):
		return carInformationQuery(condition, request, orderCondition)
	
class OrderInfoController(AdvanceSearchController):

	#
	# Order advance search
	# 
	# condition_values: an array contains all condition values
	# condition_categories: an array indicates which column is being used
	# condition_connections: an array indicates the connection between two search conditions
	# url_search_condition: search condition
	#
	# return: query result
	def order_advance_search(self, condition_values, condition_categories, condition_connections, request, url_search_condition, date_addition = "", order_sentence = ""):
		query_sentence = self.compound_query_sentence(condition_values, condition_categories, condition_connections, 'salesorder', date_addition = date_addition)
		url_search_condition['order_information'] = ""
		url_search_condition['order_information_advance'] = query_sentence
		query_sentence += order_sentence
		self.clean_stored_sorting_condition(request)
		
		return orderInformationQuery(query_sentence, request, advance = True)
		
	def order_advance_search_result(self, query_sentence, order_sentence, request):
		query_sentence += order_sentence
		return orderInformationQuery(query_sentence, request, advance = True)
		
	def order_gernal_search_result(self, condition, request, orderCondition):
		return orderInformationQuery(condition, request, orderCondition)
	
class StoreInfoController(AdvanceSearchController):

	#
	# Store advance search
	# 
	# condition_values: an array contains all condition values
	# condition_categories: an array indicates which column is being used
	# condition_connections: an array indicates the connection between two search conditions
	# url_search_condition: search condition
	#
	# return: query result
	def store_advance_search(self, condition_values, condition_categories, condition_connections, request, url_search_condition, order_sentence = ""):
		query_sentence = self.compound_query_sentence(condition_values, condition_categories, condition_connections, 'store',
					pre_query_sentence = 'SELECT * FROM store join citylist on storeCityID = cityID where ')
		url_search_condition['store_information'] = ""
		url_search_condition['store_information_advance'] = query_sentence
		query_sentence += order_sentence
		self.clean_stored_sorting_condition(request)
		
		return storeInformationQuery(query_sentence, request, advance = True)
		
	def order_advance_search_result(self, query_sentence, order_sentence, request):
		query_sentence += order_sentence
		return storeInformationQuery(query_sentence, request, advance = True)
		
	def order_gernal_search_result(self, condition, request, orderCondition):
		return storeInformationQuery(condition, request, orderCondition)
	
class CustomerInfoController(AdvanceSearchController):
	
	#
	# Customer advance search
	# 
	# condition_values: an array contains all condition values
	# condition_categories: an array indicates which column is being used
	# condition_connections: an array indicates the connection between two search conditions
	# url_search_condition: search condition
	#
	# return: query result
	def customer_advance_search(self, condition_values, condition_categories, condition_connections, request, url_search_condition, date_addition = "", order_sentence = ""):
		query_sentence = self.compound_query_sentence(condition_values, condition_categories, condition_connections, 'customer', date_addition = date_addition)
		url_search_condition['customer_information'] = ""
		url_search_condition['customer_information_advance'] = query_sentence
		query_sentence += order_sentence
		self.clean_stored_sorting_condition(request)
		
		return customerInformationSearch(query_sentence, request, advance = True)
		
		
	def order_advance_search_result(self, query_sentence, order_sentence, request):
		query_sentence += order_sentence
		return customerInformationSearch(query_sentence, request, advance = True)
		
	def order_gernal_search_result(self, condition, request, orderCondition):
		return customerInformationSearch(condition, request, orderCondition)
	
class HRManageController(AdvanceSearchController):
	
	#
	# hr advance search
	# 
	# condition_values: an array contains all condition values
	# condition_categories: an array indicates which column is being used
	# condition_connections: an array indicates the connection between two search conditions
	# url_search_condition: search condition
	#
	# return: query result
	def hr_advance_search(self, condition_values, condition_categories, condition_connections, request, url_search_condition, date_addition = "", order_sentence = ""):
		query_sentence = self.compound_query_sentence(condition_values, condition_categories, condition_connections, 'employee',
			pre_query_sentence = 'SELECT * FROM employee join citylist on employeecityid = cityID where ', date_addition = date_addition)
		
		url_search_condition['employee_management'] = ""
		url_search_condition['employee_management_advance'] = query_sentence
		query_sentence += order_sentence
		self.clean_stored_sorting_condition(request)
		
		return employeeInformationQuery(query_sentence, request, advance = True)
		
	def order_advance_search_result(self, query_sentence, order_sentence, request):
		query_sentence += order_sentence
		return employeeInformationQuery(query_sentence, request, advance = True)
		
	def order_gernal_search_result(self, condition, request, orderCondition):
		return employeeInformationQuery(condition, request, orderCondition)
		
	
class MISController(BaseSearchController):
	
	def get_city_objects(self):
		return V_Cities.objects.all()
		
	def get_VehicleMake_objects(self):
		return V_VehicleMake.objects.all() 
		
	def get_V_VehicleModel_objects(self):
		return V_VehicleModel.objects.all()
		
	def query_from_database(self):
		pass
		
	def generate_sql_select_sentence(self):
		pass
		
class AccountController(BaseController):
	
	#
	# Check if a user is exist in database
	#
	# username: username
	# password: default value: "" 
	#
	# return the result state
	def checkIfUserExist(self, username, password = ''):
		if password == '':
			namefilter = Employee.objects.filter(employeeusername=username)
			return len(namefilter) > 0
		else:
			namefilter = Employee.objects.filter(employeeusername=username, employeepassword=password)
			return len(namefilter) > 0
	
class LoginController(AccountController):
	
	#
	# Set basic information after login into session
	# 
	# such as user_access_level, username, name and the state of login
	#
	def changeSessionState(self, request, username):
		employee = Employee.objects.get(employeeusername=username)
		request.session['is_login'] = True
		request.session['user_access_level'] = employee.roleid.roleaccesslevel
		request.session['username'] = employee.employeeusername
		request.session['name'] = employee.employeefirstname + ' ' + employee.employeelastname

		request.session['update_successful'] = 0
		request.session['send_successful'] = 0
		request.session['verify_send_successful'] = 0
		
		request.session['car_information'] = ''
		request.session['order_information'] = ''
		request.session['store_information'] = ''
		request.session['customer_information'] = ''
		request.session['employee_management'] = ''
		
		request.session['car_information_advance'] = ''
		request.session['order_information_advance'] = ''
		request.session['store_information_advance'] = ''
		request.session['customer_information_advance'] = ''
		request.session['employee_management_advance'] = ''
		
class RegisterController(AccountController):

	
	#
	# Save a new employee into database
	#
	def save_new_employee(self, city, new_roleid, username, passwordfirst, email, firstname, lastname, phonenumber, address, dob):
		cityid = Citylist.objects.get(cityid=city)
		roleObject = Employeerole.objects.get(roleid = new_roleid)
		employee = Employee.objects.create(employeeusername=username, employeepassword=passwordfirst, roleid=roleObject,
					                        employeeemail=email, employeefirstname=firstname, employeelastname=lastname,
					                        employeephonenumber=phonenumber, employeecityid=cityid,
					                        employeeaddress=address, employeedob=dob)
		employee.save()


		
class ProfileController(BaseController):
	
	#
	# Get a specific user accodting to username
	#
	def get_current_user(self, username):
		currentEmployee = Employee.objects.get(employeeusername=username)
		return currentEmployee
		
class UpdateProfileController(ProfileController):

	#
	# Get current user information
	#
	def get_user_information(self, username):
		employee = self.get_current_user(username)
		default_data = {'email': employee.employeeemail, 'firstName': employee.employeefirstname, 'lastName': employee.employeelastname,
		                'phoneNumber': employee.employeephonenumber, 'city': employee.employeecityid.cityid,
		                'address': employee.employeeaddress}
		return default_data
	
	#
	# Update user profile
	#
	def updateUserProfile(self, username, email, firstname, lastname,
						phonenumber, cityid, address, request):
		employee = self.get_current_user(username)
		if (employee.employeeemail != email):
			employee.employeeemailverify = 0
		employee.employeeemail = email
		employee.employeefirstname = firstname
		employee.employeelastname = lastname
		employee.employeephonenumber = phonenumber
		employee.employeecityid = Citylist.objects.get(cityid=int(cityid))
		employee.employeeaddress = address
		employee.save()
		request.session['name'] = employee.employeefirstname + " " + employee.employeelastname


class EmailController(ProfileController):

	def message_generate(self, currentEmployee, form, request):
		if request.session['update_successful'] == 1:
			request.session['update_successful'] = 0
			success_info = 'Email address update successful, you need to reverify your email'
			return success_info
		if request.session['send_successful'] == 1:
			request.session['send_successful'] = 0
			success_info = 'Email send successful'
			return success_info
		if request.session['verify_send_successful'] == 1:
			request.session['verify_send_successful'] = 0
			success_info = 'Please confirm your email address to active email function'
		else:
			success_info = 'Null'
		return success_info

	def send_verification_email(self, request, currentEmployee):
		current_site = get_current_site(request)
		mail_subject = 'Activate your email account.'

		token = account_activation_token.make_token(currentEmployee)
		domain = current_site.domain
		uid = urlsafe_base64_encode(force_bytes(currentEmployee.pk)).decode()
		message = "\n".join(['/'.join(['http://', domain, 'employees', 'activate', uid, token])])

		to_email = currentEmployee.employeeemail
		email = EmailMessage(
			mail_subject, message, to=[to_email]
		)
		email.send()
		request.session['verify_send_successful'] = 1

	def check_email(self, new_email, currentEmployee):
		old_email = currentEmployee.employeeemail
		namefilter = Employee.objects.filter(employeeemail=new_email)

		if old_email == new_email:
			error = 'Your new email is same as old one'
			return error

		if len(namefilter) > 0:
			error = 'Your new email has been registered'
			return error
		else:
			error = 'Null'
			return error

	def update_email(self, new_email, currentEmployee, request):
		currentEmployee.employeeemail = new_email
		currentEmployee.employeeemailverify = 0
		currentEmployee.save()
		request.session['update_successful'] = 1

	def generate_user_list(self):
		userChoice = []
		for user in Employee.objects.filter(employeeemailverify=1):
			userChoice.append(user)
		return userChoice
	def send_email(self, message, currentEmployee, subject, check_box_list, request):

		to_emails = []
		for user in check_box_list:
			to_emails.append(user)

		text_content = message + '\n\n\n Send by: ' + currentEmployee.employeeusername + '\n Email: ' + currentEmployee.employeeemail
		mail = EmailMultiAlternatives(subject, text_content, bcc=to_emails)

		if request.FILES != {}:
			file = request.FILES['uploadfile']
			mail.attach(file.name, file.read(), file.content_type)

		mail.send()
		request.session['send_successful'] = 1


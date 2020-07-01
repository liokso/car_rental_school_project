#
#
# 10/09/2018
#

redirect_address = {
	'root': '/employees',
	'main': '/employees/main',
	'profile': '/employees/profile',
	'human_resource': '/employees/emp_man',
	'email': '/employees/email',
}

html_addresses = {
	'login': 'employees/login.html',
	'register': 'employees/register.html',
	'main': 'employees/main.html',
	'car_information': 'employees/car_information.html',
	'order_information': 'employees/order_information.html',
	'store_information': 'employees/store_information.html',
	'customer_information': 'employees/customer_information.html',
	'employee_management': 'employees/employee_management.html',
	'mis': 'employees/mis.html',
	'search': 'employees/search_result_test.html',
	'profile': 'employees/Profile.html',
	'update_profile': 'employees/update_profile.html',
	'email': 'employees/email.html',
	'send_email': 'employees/send_email.html',
	'update_email': 'employees/update_email.html',

}


url_data = { # All data that need to be transmitted to html page should put into this dictionary
	'cityList':'',
}

url_search_condition = { # Dictionary which used to contain Search data fro HTML file use
	'general': '',
	'car_information': '',
	'car_information_advance': '',
	'order_information': '',
	'order_information_advance': '',
	# 'order_date_condition': '',
	'store_information': '',
	'store_information_advance': '',
	'customer_information': '',
	'customer_information_advance': '',
	# 'customer_date_condition': '',
	'employee_management': '',
	'employee_management_advance': '',
	# 'employee_date_condition': '',
}	

order_category = {
	'employee': '',
	'customer': '',
}

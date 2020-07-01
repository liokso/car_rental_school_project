from django.test import TestCase
from employees.controller.DBHelper import *
from employees.controller.ViewControllers import *
from employees.controller.BaseControllers import *
from django.test.client import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware


# Create your tests here.
#

class EmployeeTest(TestCase):
	rf = RequestFactory()
	get_request = rf.get('/get/')
	post_request = rf.post('/submit/', {'foo': 'bar'})
			
	def setUp(self):
		middleware = SessionMiddleware()
		middleware.process_request(self.get_request)
		
		self.get_request.session.save()
		self.get_request.session['user_access_level'] = 5
		
		Citylist.objects.create(cityid = 1, cityname = 'Beijin', citystate = 'B')
		Citylist.objects.create(cityid = 2, cityname = 'Hangzhou', citystate = 'Z')
		Citylist.objects.create(cityid = 3, cityname = 'Nick', citystate = 'Nick')
		
		
		Employee.objects.create(employeeid = 1, employeefirstname = 'Nick', employeelastname = 'ppp', employeeusername = 'Tom', employeepassword = 'Jack',employeecityid=None,roleid=None)
		Employee.objects.create(employeeid = 2, employeefirstname = 'Nickccc', employeelastname = 'ppp', employeecityid=None,roleid=None)
		Employee.objects.create(employeeid = 3, employeefirstname = 'ick', employeelastname = 'ppp', employeecityid=None,roleid=None)
		Employee.objects.create(employeeid = 4, employeefirstname = 'aaaNick', employeelastname = 'ppp', employeecityid=None,roleid=None)
		Employee.objects.create(employeeid = 5, employeelastname = 'Nick', employeecityid=None,roleid=None)
		Employee.objects.create(employeeid = 6, employeefirstname = 'Nick', employeelastname = 'ppp', employeeaddress = 'Nick', employeecityid=None,roleid=None)
		Employee.objects.create(employeeid = 7, employeeemail = 'Nick', employeecityid=None,roleid=None)
		Employee.objects.create(employeeid = 8, employeefirstname = 'Nick', employeelastname = 'qqq', employeeusername = 'Nick', employeepassword = 'Jack', employeeloginattempt = 10, employeecityid=None, roleid=None)
		
		Customer.objects.create(customerid = 1, customerfirstname = 'Nick', customerlastname = 'ppp')
		Customer.objects.create(customerid = 2, customerfirstname = 'Nickccc', customerlastname = 'ppp')
		Customer.objects.create(customerid = 3, customerfirstname = 'ick', customerlastname = 'Nick')
		Customer.objects.create(customerid = 4, customerfirstname = 'aaaNik', customerlastname = 'ppp',)
		Customer.objects.create(customerid = 5, customerlastname = 'Nick',)
		Customer.objects.create(customerid = 6, customeraddress = 'Nick',)
		Customer.objects.create(customerid = 7, customeroccupation = 'Nick',)
		
		Store.objects.create(storeid = 1, storename = 'Nick', storeaddress = 'Left', storephonenumber = '7788', storecityid = Citylist.objects.get(cityid = 1))
		Store.objects.create(storeid = 2, storename = 'pk', storeaddress = 'Left', storephonenumber = '7788', storecityid = Citylist.objects.get(cityid = 2))
		Store.objects.create(storeid = 3, storename = 'Job', storeaddress = 'Nick', storephonenumber = '7788', storecityid = Citylist.objects.get(cityid = 3))
		Store.objects.create(storeid = 4, storename = 'Add', storeaddress = 'Left', storephonenumber = 'Nick', storecityid = Citylist.objects.get(cityid = 1))
		
		Vehicle.objects.create(vehicleid = 1, makename = 'Nick', model = 'p')
		Vehicle.objects.create(vehicleid = 2, series = 'Nick')
		Vehicle.objects.create(vehicleid = 3, seriesyear = 12)
		Vehicle.objects.create(vehicleid = 4, pricenew = 1.0)
		Vehicle.objects.create(vehicleid = 5, enginesize = 2.3)
		Vehicle.objects.create(vehicleid = 6, fuelsystem = 'Nick')
		Vehicle.objects.create(vehicleid = 7, tankcapacity = 5.0)
		Vehicle.objects.create(vehicleid = 8, power = 4.0)
		Vehicle.objects.create(vehicleid = 9, seatingcapacity = 5.0)
		Vehicle.objects.create(vehicleid = 10, standardtransmission = 'Nick')
		Vehicle.objects.create(vehicleid = 11, bodytype = 'Nick')
		Vehicle.objects.create(vehicleid = 12, wheeldrive = 'BMW')
		Vehicle.objects.create(vehicleid = 13, wheelbase  = 2.5)
		Vehicle.objects.create(vehicleid = 14, makename = 'Nick', model = 'p')
		Vehicle.objects.create(vehicleid = 15, makename = 'Nick', model = 'q')
		
		Salesorder.objects.create(orderid = 1, createdate='1990-12-24', pickupdate = '1990-12-24', 
				pickupstoreid = Store.objects.get(storeid = 1), returndate = '1990-12-24', returnstoreid = Store.objects.get(storeid = 1),
				customerid = Customer.objects.get(customerid = 1), vehicleid = Vehicle.objects.get(vehicleid = 1));
		Salesorder.objects.create(orderid = 2, createdate='1992-12-24', pickupdate = '1990-12-24', 
				pickupstoreid = Store.objects.get(storeid = 1), returndate = '1990-12-24', returnstoreid = Store.objects.get(storeid = 1),
				customerid = Customer.objects.get(customerid = 1), vehicleid = Vehicle.objects.get(vehicleid = 1));
		Salesorder.objects.create(orderid = 3, createdate='1993-12-24', pickupdate = '1993-12-24', 
				pickupstoreid = Store.objects.get(storeid = 1), returndate = '1993-12-24', returnstoreid = Store.objects.get(storeid = 1),
				customerid = Customer.objects.get(customerid = 1), vehicleid = Vehicle.objects.get(vehicleid = 1));
	
	# Test if employee general search function works
	def test_employee_info_general_search(self):		
		research_result = queryEmployee('Nick')
		self.assertEqual(len(research_result), 7)
		
	
	# Test if sorting function works fine
	def test_employee_info_sorting_with_general_search(self):
		research_result = queryEmployee('Nick', '-employeeid')
		self.assertEqual(research_result[0].employeeid, 8)
	
	# Test if employee advance search function works
	# Advance search uses raw search
	def test_employee_info_raw_search(self):
		research_result = queryEmployee('SELECT * FROM employee;', pureQuery = False)
		self.assertEqual(len(research_result), 8)
		
	# Test if customer general search function works
	def test_customer_info_general_search(self):		
		research_result = queryCustomer('Nick')
		self.assertEqual(len(research_result), 6)
	
	# Test if customer advance search function works
	# Advance search uses raw search
	def test_customer_info_raw_search(self):
		research_result = queryCustomer('SELECT * FROM customer;', pureQuery = False)
		self.assertEqual(len(research_result), 7)
		
	# Test if shop general search function works
	def test_shop_info_general_search(self):		
		research_result = queryStore('Nick')
		self.assertEqual(len(research_result), 3)
	
	# Test if shop advance search function works
	# Advance search uses raw search
	def test_shop_info_raw_search(self):
		research_result = queryStore('SELECT * FROM store;', pureQuery = False)
		self.assertEqual(len(research_result), 4)
		
	# Test if customer general search function works
	def test_car_info_general_search(self):		
		research_result = queryCar('Nick')
		self.assertEqual(len(research_result), 7)
	
	# Test if customer advance search function works
	# Advance search uses raw search
	def test_car_info_raw_search(self):
		research_result = queryCar('SELECT * FROM vehicle;', pureQuery = False)
		self.assertEqual(len(research_result), 15)
		
	# Test if customer general search function works
	def test_order_info_general_search(self):		
		research_result = queryOrder('1990')
		self.assertEqual(len(research_result), 2)
	
	# Test if customer advance search function works
	# Advance search uses raw search
	def test_order_info_raw_search(self):
		research_result = queryOrder('SELECT * FROM salesorder;', pureQuery = False)
		self.assertEqual(len(research_result), 3)
		
	#
	# Test all functions in BaseController
	#
	#
	def test_basecontroller_functions(self):
		baseController = BaseController()
		self.assertEqual(baseController.checkIfUserExist('Tom', 'Jack'), True)
		self.assertEqual(baseController.checkIfUserExist('Nick', 'Alice'), False)
		self.assertEqual(baseController.checkIfUserBan('Nick'), True)
		self.assertEqual(baseController.checkIfUserBan('Tom'), False)
	
	#
	# Test All functions in BaseSearchController
	#
	def test_baseSearchController_functions(self):
		baseSearchController = BaseSearchController()
		research_result = baseSearchController.general_search('Nick', self.get_request, employeeInformationQuery)
		self.assertEqual(research_result['employees'].paginator.count, 7)
	
	#
	# Test carInfoController
	# As all employee seach controller have the same query method.
	# CarInfoController is being chooes as a sample for test the advance search functions
	#
	def test_Controller_advance_search(self):
		carInfoController = CarInfoController()
		
		condition_values = ['Nick']
		condition_categories = ['makename']
		condition_connections = []
		url_search_condition = {}
		order_sentence = ""
		
		research_result = carInfoController.car_advance_search(condition_values, condition_categories, 
				condition_connections, self.get_request, url_search_condition)
		self.assertEqual(research_result['cars'].paginator.count, 3)
		
		condition_values = ['Nick', 'p']
		condition_categories = ['makename', 'model']
		condition_connections = ['And']
		url_search_condition = {}
		order_sentence = ""
		
		research_result = carInfoController.car_advance_search(condition_values, condition_categories, 
				condition_connections, self.get_request, url_search_condition)
		self.assertEqual(research_result['cars'].paginator.count, 2)
		
		condition_values = ['Nick', 'p', 'q']
		condition_categories = ['makename', 'model', 'model']
		condition_connections = ['And', 'Or']
		url_search_condition = {}
		order_sentence = " order by vehicleid DESC"
		
		research_result = carInfoController.car_advance_search(condition_values, condition_categories, 
				condition_connections, self.get_request, url_search_condition, order_sentence)

		self.assertEqual(research_result['cars'].paginator.count, 3)
		self.assertEqual(research_result['cars'][0].vehicleid, 15)
		
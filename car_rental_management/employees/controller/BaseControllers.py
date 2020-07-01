from ..models import *

#
# Base Controller
# father of all controller
#
class BaseController(object):

	def checkIfUserExist(self, username, password = ''):
		if password == '':
			namefilter = Employee.objects.filter(employeeusername=username)
			return len(namefilter) > 0
		else:
			namefilter = Employee.objects.filter(employeeusername=username, employeepassword=password)
			return len(namefilter) > 0

	def checkIfUserBan(self, username):
		currentUser = Employee.objects.get(employeeusername=username)
		if currentUser.employeeloginattempt >= 5:
			return True
		else:
			return False


#
# BaseSearchController
# 
# Search Controller which provide general search function
#			
class BaseSearchController(BaseController):
	
	#
	# Search data from database
	#
	# condition: search condition
	# request: request object from web page
	# search_function: search function
	#
	# return search_result: a QuerySet contains all data which matched the condition
	def general_search(self, condition, request, search_function, orderCondition = ''):
		search_result = search_function(condition, request, orderCondition)
		self.clean_stored_sorting_condition(request)
		return search_result
		
	def order_result(self, form, normal_tag, advance_tag, normal_order_method, advance_order_method, url_search_condition, request):
		order_category = form.cleaned_data['order_category']
		order_type = form.cleaned_data['order_type']
		
		normal_condition = url_search_condition[normal_tag]
		advance_condition = url_search_condition[advance_tag]
		
		order_sentence = ''
			
		if advance_condition == '':
			if order_type == 'ascending':
				order_sentence = order_category
			else:
				order_sentence = '-' + order_category
			
			self.change_requst_sorting_info(normal_tag, order_sentence, request)
			return normal_order_method(normal_condition, request, order_sentence)
		else:
			order_sentence = ' order by ' + order_category
			if order_type != 'ascending':
				order_sentence += ' DESC'
				
			self.change_requst_advance_sorting_info(advance_tag, order_sentence, request)
			
			# if date_addition != '':
				# return advance_order_method(advance_condition, order_sentence, request, date_addition)
			return advance_order_method(advance_condition, order_sentence, request)
			
	def change_requst_sorting_info(self, normal_tag, order_sentence, request):
		normal_tags = ('car_information', 'order_information', 'store_information', 'customer_information', 'employee_management',)
		
		for condition in normal_tags:
			if str(condition) != str(normal_tag):
				request.session[condition] = ""
			else:
				request.session[condition] = order_sentence

	def change_requst_advance_sorting_info(self, advance_tag, order_sentence, request):
		advance_tags = ('car_information_advance', 'order_information_advance', 'store_information_advance', 'customer_information_advance', 'employee_management_advance',)
		
		for condition in advance_tags:
			if str(condition) != str(advance_tag):
				request.session[condition] = ""
			else:
				request.session[condition] = order_sentence
	
	def clean_stored_sorting_condition(self, request):
		normal_tags = ('car_information', 'order_information', 'store_information', 'customer_information', 'employee_management',)
		advance_tags = ('car_information_advance', 'order_information_advance', 'store_information_advance', 'customer_information_advance', 'employee_management_advance',)
		compand_tags = normal_tags + advance_tags
		for tags in compand_tags:
			request.session[tags] = ""
			
		

#
# Advance Search Controler
# Contains some general advance search functions
#		
class AdvanceSearchController(BaseSearchController):
	
	#
	# Compund query sentence according to user input as it use raw query
	#
	# condition_values: an array contains all condition values
	# condition_categories: an array indicates which column is being used
	# condition_connections: an array indicates the connection between two search conditions
	# table_name: name of table
	#
	# return: a query sentence
	def compound_query_sentence(self, condition_values, condition_categories, condition_connections, table_name, pre_query_sentence = "", date_addition = ""):
		if len(condition_categories) > 0 and len(condition_values) > 0:
			if pre_query_sentence == "":
				query_sentence = "SELECT * FROM " + table_name + " WHERE "
			else:
				query_sentence = pre_query_sentence
			query_sentence += condition_categories[0] + " LIKE '%%" + condition_values[0] + "%%'"
			for index in range(1, len(condition_categories)):
				category_name = condition_categories[index]
				query_sentence += " " + condition_connections[index - 1] + " " + condition_categories[index] + " LIKE '%" + condition_values[index] + "%' "
			if date_addition != "":
				query_sentence += " AND " + date_addition + ""
			return query_sentence
		elif date_addition != "":
			query_sentence = "SELECT * FROM " + table_name + " WHERE " + date_addition + ""
			return query_sentence;
		return "SELECT * FROM " + table_name + "";
	#
	# Reload advance data
	# 
	# query_sentence:query sentence
	# request:request object
	# query_function: query function
	def reload_advance_data(self, query_sentence, request, query_function):
		return query_function(query_sentence, request, advance = True)
		
class DateAdvanceSearchResultController(AdvanceSearchController):
	
	#
	# Create a date query sentence based on existed sentence
	#
	# origin_sentence: query sentence
	# column_name: column name
	# date_object: date object from website
	#
	# return: a new sentence
	def create_date_query_sentence(self, origin_sentence, column_name, date_object, if_start): 
		if date_object != None:
			date_object = date_object.strftime('%Y-%m-%d')
			if origin_sentence == "":
				if if_start:
					origin_sentence = column_name + " >= '" +  date_object + "' "
				else:
					origin_sentence = column_name + " <= '" +  date_object + "' "
			else:
				if if_start:
					origin_sentence += "AND " + column_name + " >= '" + date_object + "' "
				else:
					origin_sentence += "AND " + column_name + " <= '" + date_object + "' "
		return origin_sentence
		
from django.shortcuts import render, redirect
from django.views import View

from .forms import *
from .models import *
from .controller.DBHelper import *
from .controller.Search import *
from .controller.ViewControllers import *

from django.http import HttpResponse

from .utils.html_data_helper import *
# Search functions has been created in DBHelper.py

#
# Base View
# 
# every subclass should rewrite 'address'
# every subclass should rewrite 'pre_get' and 'pre_post' which will be processed in 'get' and 'post' functions
#
# If subclasses need to redirect, rewrite 'get' and 'post' functions
class BaseView(View):
	result_data = {} # data which will be transported to web page
	address = "" # url address relates to a specific View
	
	def pre_get(self, request):
		pass
	
	def pre_post(self, request):
		pass
	
	#
	# Check if current user logs into this system
	#
	def dispatch(self, request, *args, **kwargs):
		user_info = request.session.get('is_login', None)
		if not user_info:
			return redirect(redirect_address['root'])
		return super().dispatch(request, *args, **kwargs)
	
	#
	# Response for a get request from web page
	#
	def get(self, request, *args, **kwargs):
		self.pre_get(request)
		return render(request, self.address, self.result_data)	
	
	#
	# Response for a post request from web page
	#
	def post(self, request, *args, **kwargs):
		self.pre_post(request);
		return render(request, self.address, self.result_data)
#
#	A general search result View
#
class SearchResultView(BaseView):
	searchController = SearchResultController() 
	address = html_addresses['search']
	
	def pre_get(self, request):
		self.result_data = self.searchController.general_search(url_search_condition['general'], request, generalQuery)
	
	def pre_post(self, request):
		form = GeneralSearchForm(request.POST)
		
		if form.is_valid():
			url_search_condition['general'] = form.cleaned_data['search_condition']
		else:
			url_search_condition['general'] = ''
		
		search_result = self.searchController.general_search(url_search_condition['general'], request, generalQuery)
		
		if len(search_result) <= 0:
			url_search_condition['general'] = ''
			
		self.result_data = search_result
				

		
			

#
# Advance 
# 
#			
class AdvanceSearchResultView(SearchResultView):
	
	#
	# Checl values in each array to make sure all of them are matched
	#
	# conditions: conditions array
	# categories: categories array
	# connections: connections array
	#
	def value_checker(self, conditions, categories, connections):
		index = 0		
		while index < len(conditions):
			if conditions[index] == '':
				conditions.remove(conditions[index])
				categories.remove(categories[index])
				connections.remove(connections[index])
			else:
				index = index + 1
	
	# def manipulate_form_date(self):
		# self.value_checker(conditions, categories, connections)
	
	#
	# Get values from conditions form
	#
	# form
	#
	# return: a condition array
	def get_condition_values(self, form):
		first_condition = form.cleaned_data['first_condition'] # good
		second_condition = form.cleaned_data['second_condition']
		third_condition = form.cleaned_data['third_condition']
		fourth_condition = form.cleaned_data['fourth_condition']
		fifth_condition = form.cleaned_data['fifth_condition']
		
		conditions = [first_condition, second_condition, third_condition, fourth_condition, fifth_condition]
		return conditions
	
	#
	# Get values from categories form
	#
	# form
	#
	# return: a condition array	
	def get_categories_values(self, form):
		first_category = form.cleaned_data['first_category']
		second_category = form.cleaned_data['second_category']
		third_category = form.cleaned_data['third_category']
		fourth_category = form.cleaned_data['fourth_category']
		fifth_category = form.cleaned_data['fifth_category']
		
		categories = [first_category, second_category, third_category, fourth_category, fifth_category]
		return categories
	
	#
	# Get values from connections form
	#
	# form
	#
	# return: a condition array
	def get_connections_values(self, form):
		first_connection = form.cleaned_data['first_connection']
		second_connection = form.cleaned_data['second_connection']
		third_connection = form.cleaned_data['third_connection']
		fourth_connection = form.cleaned_data['fourth_connection']
		fifth_connection = form.cleaned_data['fifth_connection']		
		
		connections = [first_connection, second_connection, third_connection, fourth_connection, fifth_connection]
		return connections
	
	#
	# advance query
	#
	# form: form object
	# search_function: search function
	# url_search_condition: condition
	# request: object
	#
	# return: the search result
	def query_advance_conditoin_result(self, form, search_function, url_search_condition, request):
		conditions = self.get_condition_values(form)
		categories = self.get_categories_values(form)
		connections = self.get_connections_values(form)
		
		self.value_checker(conditions, categories, connections)
		return search_function(conditions, categories, connections, request, url_search_condition)
		
# Hint:
#	Please overwrite get_date_query_sentence function 		
class DateAdvanceSearchResultView(AdvanceSearchResultView):

	dateAdvanceSearchResultController = DateAdvanceSearchResultController()
	
	def create_date_query_sentence(self, origin_sentence, column_name, date_object, if_start): 
		return self.dateAdvanceSearchResultController.create_date_query_sentence(origin_sentence, column_name, date_object, if_start)
		
	# def query_advance_with_date_result(self, form, search_function, url_search_condition, date_addition, request):
		# conditions = self.get_condition_values(form)
		# categories = self.get_categories_values(form)
		# connections = self.get_connections_values(form)
		
		# self.value_checker(conditions, categories, connections)
		
		# return search_function(conditions, categories, connections, request, url_search_condition, date_addition)
	
	def get_date_query_sentence(self, form, request):
		return ""
		
	def query_advance_conditoin_result(self, form, search_function, url_search_condition, request):		
		conditions = self.get_condition_values(form)
		categories = self.get_categories_values(form)
		connections = self.get_connections_values(form)
		
		self.value_checker(conditions, categories, connections)
		date_addition = self.get_date_query_sentence(form)
		return search_function(conditions, categories, connections, request, url_search_condition, date_addition)
		
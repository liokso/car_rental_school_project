from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from customers.utils.html_data_helper import *
from django.views import View
from employees.controller.ViewControllers import *
from employees.controller.DBHelper import *
#from customers.controller.ViewControllers import *
from .views import *
from employees.forms import *
from employees.models import *
from customers.models import *
from django.db.models import Max, Count, Q
from datetime import datetime, timedelta
from django.db import connection

def get_date(rawquery_set):
	array = []
	for obj in rawquery_set:
		array.append(obj)
	return array

# Create your views here.
def car_info(request):
	if request.method == 'POST':
		form = CarInformationForm(request.POST)
		if form.is_valid():
			url_search_condition['car_information'] = form.cleaned_data['search_condition']
			return render(request, html_addresses['car_information'])
		else:
			pass
	results = Salesorder.objects.all().aggregate(Max('returndate'))['returndate__max']
	results = results - timedelta(days = 90)


	query_result = Salesorder.objects.filter(pickupdate__gte = results).values('vehicleid').annotate(num=Count('vehicleid')).order_by('-num')

	#recommand_result = dict(query_result.items()[0:3])

	recommand_result = []
	index = 0
	for obj in query_result:
		recommand_result.append(obj)
		index += 1
		if index > 2:
			break
		#import pdb;pdb.set_trace()

	return render(request, 'customers/search.html', {'recommand' :recommand_result})



# class CarInfoView(SearchResultView):
# 	carController = CarInfoController()
# 	address = html_addresses['car_information']
#
# 	def pre_get(self, request):
# 		self.reload_general_search_result(carInformationQuery, request, 'car_information')
#
# 	def pre_post(self, request):
# 		self.general_search(CarInformationForm, carInformationQuery, request, 'car_information')
class CarInfoView(View):
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

class CarView(generic.ListView):
	template_name = 'customers/car_list.html'
	condition = ""


	def post(self, request, *args, **kwargs):
		form = CarInformationForm(request.POST)
		#import pdb;pdb.set_trace()
		if form.is_valid():
			self.condition = form.cleaned_data['search_condition']

		self.object_list = self.get_queryset()
		allow_empty = self.get_allow_empty()

		if not allow_empty:
			# When pagination is enabled and object_list is a queryset,
			# it's better to do a cheap query than to load the unpaginated
			# queryset in memory.
			if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
				is_empty = not self.object_list.exists()
			else:
				is_empty = not self.object_list
			if is_empty:
				raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.") % {
					'class_name': self.__class__.__name__,
				})
		context = self.get_context_data()
		return self.render_to_response(context)

	def get_queryset(self):
		#return Vehicle.objects.filter(makename__contains=self.condition)
		p = queryCar(self.condition, order_condition = '-pricenew')
		return p

class DetailView(generic.DetailView):

	model = Vehicle
	template_name = 'customers/car_detail.html'

	def get(self, request, *args, **kwargs):
		car = Vehicle.objects.get(vehicleid=kwargs['pk'])
		return render(request, html_addresses['car_detail'], {'car': car})

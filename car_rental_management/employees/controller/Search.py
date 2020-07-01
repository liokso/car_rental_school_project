from django.shortcuts import render
from ..utils.html_data_helper import *

# The main search function
#
# html_address: the address of the webpage which user want to go
# FormConstructor: the name of form class which will be used for search
# request: request object
# search_condition_name: the name of search condition which used to store search condition

# return HttpRequest object and result data
def search_main(html_address, FormConstructor, search_function, request, search_condition_name):
	global url_search_condition
	if request.method == 'POST':
		form = FormConstructor(request.POST)
		if form.is_valid():
			url_search_condition[search_condition_name] = form.cleaned_data['search_condition']
		else:
			url_search_condition[search_condition_name] = ''
		
		search_result = search_function(url_search_condition[search_condition_name], url_data['currentUserAccessLevel'], request)
		
		if len(search_result) <= 0:
			url_data['empty'] = 1
			url_search_condition[search_condition_name] = ''
			return render(request, html_address, url_data)

		
		result_data = {**url_data, **search_result}
		return render(request, html_address, result_data)
	else:
		url_data['empty'] = 0
		search_result = search_function(url_search_condition[search_condition_name], url_data['currentUserAccessLevel'], request)
		result_data = {**url_data, **search_result}
		return render(request, html_address, result_data)	
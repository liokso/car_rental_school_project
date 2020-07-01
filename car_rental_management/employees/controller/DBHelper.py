#
# Person.objects.raw('SELECT * FROM myapp_person'):
#
from django.db.models import Q
from django.db.models.query import RawQuerySet
from django.core.paginator import Paginator
from ..models import *
from django.db import connection

#
# Query Car information
#
# condition: search conditoin
# order_condition: order condition such as '-pickupdate' <DESC for 'pickupdate' column>
# pureQuery: if select everything
#
# return queryset
def queryCar(condition, order_condition = '', pureQuery = True):
	if pureQuery:
		querySet = Vehicle.objects.filter(Q(makename__contains=condition) | Q(model__contains=condition) |
			Q(series__contains=condition) | Q(bodytype__contains=condition) | Q(seriesyear__contains=condition) |
			Q(pricenew__contains=condition) | Q(enginesize__contains=condition) | Q(fuelsystem__contains=condition) |
			Q(tankcapacity__contains=condition) |Q(standardtransmission__contains=condition) | Q(power__contains=condition) |
			Q(seatingcapacity__contains=condition) |
			Q(wheeldrive__contains=condition) | Q(wheelbase__contains=condition) | Q(vehicleid__contains=condition))
	else:
		querySet = Vehicle.objects.raw(condition)
		
	if order_condition == '':
		return querySet
	else:
		return querySet.order_by(order_condition)

#
# Query Store information
#
# condition: search conditoin
# order_condition: order condition such as '-pickupdate' <DESC for 'pickupdate' column>
# pureQuery: if select everything
#
# return queryset
def queryStore(condition, order_condition = '', pureQuery = True):
	if pureQuery:
		querySet = Store.objects.filter(Q(storename__contains=condition) | Q(storeaddress__contains=condition) | Q(storephonenumber__contains=condition) |
			Q(storeid__contains=condition) | Q(storecityid__citystate__contains=condition) | Q(storecityid__cityname__contains=condition))
	else:
		querySet = Store.objects.raw(condition)
		
	if order_condition == '':
		return querySet
	else:
		return querySet.order_by(order_condition)

#
# Query Order information
#
# condition: search conditoin
# order_condition: order condition such as '-pickupdate' <DESC for 'pickupdate' column>
# pureQuery: if select everything
#
# return queryset
def queryOrder(condition, order_condition = '', pureQuery = True):
	if pureQuery:
		querySet = Salesorder.objects.filter(Q(orderid__contains=condition) | Q(createdate__contains=condition) | Q(vehicleid__vehicleid__contains=condition) |
		                                     Q(customerid__customerid__contains=condition) | Q(pickupstoreid__storeid__contains=condition) |
		                                     Q(returnstoreid__storeid__contains=condition) | Q(pickupdate__contains=condition) | Q(returndate__contains=condition))
	else:
		querySet = Salesorder.objects.raw(condition)
		
	if order_condition == '':
		return querySet
	else:
		return querySet.order_by(order_condition)


#
# Query Customer information
#
# condition: search conditoin
# order_condition: order condition such as '-pickupdate' <DESC for 'pickupdate' column>
# pureQuery: if select everything
#
# return queryset
def queryCustomer(condition, order_condition = '', pureQuery = True):
	if pureQuery:
		querySet = Customer.objects.filter(Q(customerfirstname__contains=condition) | Q(customerlastname__contains=condition) |
			Q(customeraddress__contains=condition) | Q(customeroccupation__contains=condition) | Q(customerdob__contains=condition) | Q(customerid__contains=condition))
	else:
		querySet = Customer.objects.raw(condition)
			
	if order_condition == '':
		return querySet
	else:
		return querySet.order_by(order_condition)


#
# Query Employee information
#
# condition: search conditoin
# order_condition: order condition such as '-pickupdate' <DESC for 'pickupdate' column>
# pureQuery: if select everything
#
# return queryset
def queryEmployee(condition, order_condition = '', pureQuery = True):
	if pureQuery:
		querySet = Employee.objects.filter(Q(employeelastname__contains=condition) | Q(employeefirstname__contains=condition) |
			Q(employeeaddress__contains=condition) | Q(employeeemail__contains=condition) |
			Q(employeeusername__contains=condition) | Q(employeeid__contains=condition) |
			Q(employeecityid__citystate__contains=condition) | Q(employeecityid__cityname__contains=condition))
	else:
		querySet = Employee.objects.raw(condition)
	
	if order_condition == '':
		return querySet
	else:
		return querySet.order_by(order_condition)


#
# Pagining data 
#
# querysetData: query set data
# request: request object
# name: name of the paginator
def pagingSet(querysetData, request, name):
	paginator = Paginator(querysetData, 20)
	page = request.GET.get(name)
	dataForOnePage = paginator.get_page(page)
	return dataForOnePage

#
# Combine search data set into one dictionary
#
# querySet: the query set need to be sotred into dictionary
# setName: the index name for this query set
# storeDict: the dictionary container
# request: request object
#
# return storeDict	
def conbineSearchData(querySet, setName, storeDict, request):
	if querySet.count() > 0:
		storeDict[setName] = pagingSet(querySet, request, setName)
		return storeDict
	return storeDict

#
# General Query (Query everything)
# 
# condition: search condition
# request: request object
# order_condition: order condition such as '-pickupdate' <DESC for 'pickupdate' column>
#
# return the dictionary contains all information
def generalQuery(condition, request, order_condition = ''):
	search_result = {}
	if request.session['user_access_level'] >= 5:
		employeeQueryset = queryEmployee(condition)
		search_result = conbineSearchData(employeeQueryset, 'employees', search_result, request)
	customerQueryset = queryCustomer(condition)
	orderQueryset = queryOrder(condition)
	storeQueryset = queryStore(condition)
	carQueryset = queryCar(condition)
	
	search_result = conbineSearchData(customerQueryset, 'customers', search_result, request)
	search_result = conbineSearchData(storeQueryset, 'stores', search_result, request)
	search_result = conbineSearchData(orderQueryset, 'orders', search_result, request)
	search_result = conbineSearchData(carQueryset, 'cars', search_result, request)

	return search_result

#
# Count the result, check if any data is been founded
#
# querySet: a set of query result
#
# return the length of the queryset
def count(querySet):
	if type(querySet) == RawQuerySet:
		length = sum(1 for result in querySet)
		return length
	else:
		return querySet.count()

#
# Query car information 
# 
# condition: query condition
# request: request object
# order_condition: order condition such as '-pickupdate' <DESC for 'pickupdate' column>
# advance: if use advance search
#
# return: the result		
def carInformationQuery(condition, request, order_condition = '', advance = False):
	search_result = {}

	if request.session['user_access_level'] >= 2:
		if advance:
			carQueryset = queryCar(condition, order_condition = '', pureQuery = False)
		else:
			carQueryset = queryCar(condition, order_condition = order_condition)
		if count(carQueryset) > 0:
			search_result['cars'] = pagingSet(carQueryset, request, 'cars')
	return search_result

#
# Query order information 
# 
# condition: query condition
# request: request object
# order_condition: order condition such as '-pickupdate' <DESC for 'pickupdate' column>
# advance: if use advance search
#
# return: the result
def orderInformationQuery(condition, request, order_condition = '', advance = False):
	search_result = {}
	if request.session['user_access_level'] >= 2:
		if advance:
			orderQueryset = queryOrder(condition, order_condition = '', pureQuery = False)
		else:
			orderQueryset = queryOrder(condition, order_condition = order_condition)
		# if orderQueryset.count() > 0:
		if count(orderQueryset) > 0:
			search_result['orders'] = pagingSet(orderQueryset, request, 'orders')
	return search_result

#
# Query employee information 
# 
# condition: query condition
# request: request object
# order_condition: order condition such as '-pickupdate' <DESC for 'pickupdate' column>
# advance: if use advance search
#
# return: the result
def employeeInformationQuery(condition, request, order_condition = '', advance = False):
	search_result = {}
	if request.session['user_access_level'] >= 5:
		if advance:
			employeeQueryset = queryEmployee(condition, order_condition = '', pureQuery = False)
		else:
			employeeQueryset = queryEmployee(condition, order_condition = order_condition)
		# if employeeQueryset.count() > 0:
		if count(employeeQueryset) > 0:
			search_result['employees'] = pagingSet(employeeQueryset, request, 'employees')
	return search_result
#
# Query store information 
# 
# condition: query condition
# request: request object
# order_condition: order condition such as '-pickupdate' <DESC for 'pickupdate' column>
# advance: if use advance search
#
# return: the result
def storeInformationQuery(condition, request, order_condition = '', advance = False):
	search_result = {}
	if request.session['user_access_level'] >= 2:
		if advance:
			storeQueryset = queryStore(condition, order_condition = '', pureQuery = False)
		else:
			storeQueryset = queryStore(condition, order_condition = order_condition)
		# if storeQueryset.count() > 0:
		if count(storeQueryset) > 0:
			search_result['stores'] = pagingSet(storeQueryset, request, 'stores')
	return search_result
	
#
# Query customer information 
# 
# condition: query condition
# request: request object
# order_condition: order condition such as '-pickupdate' <DESC for 'pickupdate' column>
# advance: if use advance search
#
# return: the result
def customerInformationSearch(condition, request, order_condition = '', advance = False):
	
	search_result = {}
	if request.session['user_access_level'] >= 2:
		if advance:
			customerQueryset = queryCustomer(condition, order_condition = '', pureQuery = False)
		else:
			customerQueryset = queryCustomer(condition, order_condition = order_condition)
		# if customerQueryset.count() > 0:
		if count(customerQueryset) > 0:
			search_result['customers'] = pagingSet(customerQueryset, request, 'customers')
	return search_result
		
		
def GetListofCities():
	result = V_Cities.objects.all()
	return result
	
def MISquery(sqlQuery):
	cursor = connection.cursor()
	cursor.execute(sqlQuery)
	resultMIS = cursor.fetchall()
	return resultMIS

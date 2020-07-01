from django.db.models import Q
from django.core.paginator import Paginator
from ..models import *


def queryCar(condition, pureQuery = True):
	if pureQuery:
		querySet = Vehicle.objects.filter(Q(makename__contains=condition) | Q(model__contains=condition) |
			Q(series__contains=condition) | Q(bodytype__contains=condition) | Q(seriesyear__contains=condition) |
			Q(pricenew__contains=condition) | Q(enginesize__contains=condition) | Q(fuelsystem__contains=condition) |
			Q(tankcapacity__contains=condition) |Q(standardtransmission__contains=condition) | Q(power__contains=condition) |
			Q(seatingcapacity__contains=condition) |
			Q(wheeldrive__contains=condition) | Q(wheelbase__contains=condition) | Q(vehicleid__contains=condition))
		return querySet
	pass

def carInformationSearch(condition, currentUserAccessLevel, request):
	search_result = {}
	if currentUserAccessLevel >= 2:
		carQUeryset = queryCar(condition)
		if carQUeryset.count() > 0:
			search_result['cars'] = pagingSet(carQUeryset, request, 'cars')
		if len(search_result) == 0:
			search_result['empty'] = 1
		return search_result
	else:
		return {}

def generySearch(condition, currentUserAccessLevel, request):
	search_result = {}
	if currentUserAccessLevel >= 5:
		carQueryset = queryCar(condition)
		search_result = conbineSearchData(carQueryset, 'cars', search_result, request)

		if len(search_result) == 0:
			search_result['empty'] = 1
			return search_result
		return search_result


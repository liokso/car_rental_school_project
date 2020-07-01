from customers.models import *


class BaseController(object):
    def checkIfUserExist(self, username, password=''):
        if password == '':
            namefilter = Employee.objects.filter(employeeusername=username)
            return len(namefilter) > 0
        else:
            namefilter = Employee.objects.filter(employeeusername=username, employeepassword=password)
            return len(namefilter) > 0


class BaseSearchController(BaseController):

    def general_search(self, FormConstructor, search_function, request, search_condition_name, url_search_condition):
        form = FormConstructor(request.POST)

        if form.is_valid():
            url_search_condition[search_condition_name] = form.cleaned_data['search_condition']
        else:
            url_search_condition[search_condition_name] = ''

        search_result = search_function(url_search_condition[search_condition_name],
                                        request.session['user_access_level'], request)

        if len(search_result) <= 0:
            url_search_condition[search_condition_name] = ''

        return search_result

    def reload_search_result(self, search_function, request, search_condition_name, url_search_condition):
        search_result = search_function(url_search_condition[search_condition_name],
                                        request.session['user_access_level'], request)
        return search_result
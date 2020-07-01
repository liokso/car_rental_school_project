from .BaseControllers import *
from ..models import *
from .DBHelper import *


class MainController(BaseController):
    def get_car_remaining(self):

        return 100

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


class SearchResultController(BaseSearchController):
    pass


class CarInfoController(BaseSearchController):
    pass


class OrderInfoController(BaseSearchController):
    pass


class StoreInfoController(BaseSearchController):
    pass


class CustomerInfoController(BaseSearchController):
    pass


class HRManageController(BaseSearchController):
    pass


class MISController(BaseSearchController):

    def get_city_objects(self):
        return V_Cities.objects.all()


class LoginController(BaseController):

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


class RegisterController(BaseController):

    #
    # Save a new employee into database
    #
    def save_new_employee(self, city, new_roleid, username, passwordfirst, email, firstname, lastname, phonenumber,
                          address, dob):
        cityid = Citylist.objects.get(cityid=city)
        roleObject = Employeerole.objects.get(roleid=new_roleid)
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
        default_data = {'email': employee.employeeemail, 'firstName': employee.employeefirstname,
                        'lastName': employee.employeelastname,
                        'phoneNumber': employee.employeephonenumber, 'city': employee.employeecityid.cityid,
                        'address': employee.employeeaddress}
        return default_data

    #
    # Update user profile
    #
    def updateUserProfile(self, username, email, firstname, lastname,
                          phonenumber, cityid, address, request):
        employee = self.get_current_user(username)
        employee.employeeemail = email
        employee.employeefirstname = firstname
        employee.employeelastname = lastname
        employee.employeephonenumber = phonenumber
        employee.employeecityid = Citylist.objects.get(cityid=int(cityid))
        employee.employeeaddress = address
        employee.save()
        request.session['username'] = employee.employeefirstname + " " + employee.employeelastname
from django import forms
from .models import *


class SignUpForm(forms.Form):
	salePerson = '2'
	manager = '1'
	roleIDChoice = (
		(salePerson, 'Sale person'),
		(manager, 'Manager'),
	)

	DOY = ('1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947',
	       '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955',
	       '1954', '1957', '1958', '1959', '1960', '1961', '1962', '1963',
	       '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971',
	       '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979',
	       '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
	       '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
	       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
	       '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
	       '2012', '2013', '2014', '2015', '2016', '2017', '2018')

	cityidChoice = (
		('1', 'Alexandria'), ('2', 'Bendigo'), ('3', 'Brisbane'), ('4', 'Caloundra'), ('5', 'Cloverdale'),
		('6', 'Coffs Harbour'), ('7', 'Cranbourne'), ('8', 'Darlinghurst'), ('9', 'East Brisbane'), ('10', 'Findon'),
		('11', 'Geelong'), ('12', 'Gold Coast'), ('13', 'Goulburn'), ('14', 'Hawthorne'), ('15', 'Harvey Bay'),
		('16', 'Hobart'), ('17', 'Lane Cove'), ('18', 'Lavender Bay'), ('19', 'Malabar'), ('20', 'Matraville'),
		('21', 'Melbourne'), ('22', 'Melton'), ('23', 'Milsons Point'), ('24', 'Newcastle'), ('25', 'North Ryde'),
		('26', 'North Sydney'), ('27', 'Perth'), ('28', 'Port Macquarie'), ('29', 'Rhodes'), ('30', 'Rockhampton'),
		('31', 'Seaford'), ('32', 'Sliverwater'), ('33', 'South Melbourne'), ('34', 'Springwood'),
		('35', 'St. Leonards'), ('36', 'Sunbury'), ('37', 'Sydney'), ('38', 'Townsville'), ('39', 'Warrnambool'),
		('40', 'Wollongong'),
	)

	username = forms.CharField(label='Username  ', max_length=50, help_text='Set your username')
	passwordSet = forms.CharField(label='Password   ', widget=forms.PasswordInput(), help_text='Input your password')
	passwordEnsure = forms.CharField(label='Ensure Password   ', widget=forms.PasswordInput(), help_text='Input your password again')
	roleID = forms.ChoiceField(label='Role   ', choices=roleIDChoice, help_text='Choose your role ID')
	email = forms.EmailField(label='Email   ', max_length=100, help_text='Set your email')
	firstName = forms.CharField(label='FirstName   ', max_length=50, help_text='Set your FirstName')
	lastName = forms.CharField(label='LastName   ', max_length=50, help_text='Set your LastName')
	phoneNumber = forms.CharField(label='Phone Number   ', max_length=11, help_text='Input your phone number')
	city = forms.ChoiceField(label='City   ', choices=cityidChoice, help_text='Choose your city')
	address = forms.CharField(label='Address   ', max_length=50, help_text='Set your living address')
	DOB = forms.DateField(label='Birth day   ', widget=forms.SelectDateWidget(years=DOY), help_text='Set your birthday')


class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=50)
	password = forms.CharField(label='Password', widget=forms.PasswordInput())

class GeneralSearchForm(forms.Form):
	search_condition = forms.CharField(initial='', required=False)
	
class AdvanceSearchForm(GeneralSearchForm):
	connection_categories = (('And', 'And'), ('Or', 'Or'), ('Choose', 'Choose'))

	first_condition  = forms.CharField(initial='', required=False)
	second_condition = forms.CharField(initial='', required=False)
	third_condition  = forms.CharField(initial='', required=False)
	fourth_condition  = forms.CharField(initial='', required=False)
	fifth_condition  = forms.CharField(initial='', required=False)
	
	first_connection = forms.ChoiceField(choices=connection_categories, required=False) # added later
	second_connection = forms.ChoiceField(choices=connection_categories, required=False)
	third_connection = forms.ChoiceField(choices=connection_categories, required=False)
	fourth_connection = forms.ChoiceField(choices=connection_categories, required=False)
	fifth_connection  = forms.ChoiceField(choices=connection_categories, required=False)

class CarInformationForm(AdvanceSearchForm):
	searchCategory = (
		('makename', 'makeName'), ('model', 'model'), ('series', 'series'), ('seriesyear', 'seriesYear'), ('pricenew', 'priceNew'),
		('enginesize', 'engineSize'), ('fuelsystem', 'fuelSystem'), ('tankcapacity', 'tankCapacity'),
		('power', 'power'), ('seatingcapacity', 'seatingCapacity'), ('standardtransmission', 'standardTransmission'),
		('bodytype', 'bodyType'), ('wheeldrive', 'wheelDrive'), ('wheelbase', 'wheelBase'),
	)
	
	orderCategory = searchCategory + (('vehicleid', 'vehicle id'),)
	orderTypeCategory = (('ascending', 'ascending'), ('descending', 'descending'),)
	
	first_category = forms.ChoiceField(choices=searchCategory, required=False, initial='makename')
	second_category = forms.ChoiceField(choices=searchCategory, required=False, initial='makename')
	third_category = forms.ChoiceField(choices=searchCategory, required=False, initial='makename')
	fourth_category = forms.ChoiceField(choices=searchCategory, required=False, initial='makename')
	fifth_category = forms.ChoiceField(choices=searchCategory, required=False, initial='makename')
	
	order_category = forms.ChoiceField(choices=orderCategory, required=False, initial='id')
	order_type = forms.ChoiceField(choices=orderTypeCategory, required=False, initial='ascending')

class OrderInformationForm(AdvanceSearchForm):
	searchCategory = (
		('pickupstoreid', 'pickupstoreid'), ('returnstoreid', 'returnstoreid'),
		('customerid', 'customerid'), ('vehicleid', 'vehicleid')
	)
	# ('createdate', 'createdate'), ('pickupdate', 'pickupdate'), ('returndate', 'returndate'), 
	orderCategory = searchCategory + (('orderid', 'id'),
				('createdate', 'createdate'), ('pickupdate', 'pickupdate'), ('returndate', 'returndate'),)
	orderTypeCategory = (('ascending', 'ascending'), ('descending', 'descending'),)
	
	first_category = forms.ChoiceField(choices=searchCategory, required=False, initial='createdate')
	second_category = forms.ChoiceField(choices=searchCategory, required=False, initial='createdate')
	third_category = forms.ChoiceField(choices=searchCategory, required=False, initial='createdate')
	fourth_category = forms.ChoiceField(choices=searchCategory, required=False, initial='createdate')
	fifth_category = forms.ChoiceField(choices=searchCategory, required=False, initial='createdate')
	
	start_date_create = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',), required=False)
	end_date_create = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',), required=False)
	
	start_date_pick = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',), required=False)
	end_date_pick = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',), required=False)
	
	start_date_return = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',), required=False)
	end_date_return = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',), required=False)
	
	order_category = forms.ChoiceField(choices=orderCategory, required=False, initial='id')
	order_type = forms.ChoiceField(choices=orderTypeCategory, required=False, initial='ascending')

class EmployeeInformationForm(AdvanceSearchForm):
	searchCategory = (
		('employeefirstname', 'employeefirstname'), ('employeelastname', 'employeelastname'), 
		('employeeaddress', 'employeeaddress'), ('cityname', 'cityname'), ('citystate', 'citystate'),
		('employeeemail', 'employeeemail'), ('employeephonenumber', 'employeephonenumber'),
	)
	
	orderCategory = searchCategory + (('employeedob', 'dob'), ('employeeid', 'id'),)
	# orderCategory = (
		# ('employeefirstname', 'employeefirstname'), ('employeelastname', 'employeelastname'), 
		# ('employeeaddress', 'employeeaddress'), ('cityname', 'cityname'), ('citystate', 'citystate'),
		# ('employeeemail', 'employeeemail'), ('employeephonenumber', 'employeephonenumber'), ('employeedob', 'dob'), ('employeeid', 'id'), 
	# )
	orderTypeCategory = (('ascending', 'ascending'), ('descending', 'descending'),)
	# ('employeedob', 'employeedob'), 
	
	first_category = forms.ChoiceField(choices=searchCategory, required=False, initial='employeefirstname')
	second_category = forms.ChoiceField(choices=searchCategory, required=False, initial='employeefirstname')
	third_category = forms.ChoiceField(choices=searchCategory, required=False, initial='employeefirstname')
	fourth_category = forms.ChoiceField(choices=searchCategory, required=False, initial='employeefirstname')
	fifth_category = forms.ChoiceField(choices=searchCategory, required=False, initial='employeefirstname')
	
	start_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',), required=False)
	end_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',), required=False)
	
	order_category = forms.ChoiceField(choices=orderCategory, required=False, initial='id')
	order_type = forms.ChoiceField(choices=orderTypeCategory, required=False, initial='ascending')

class StoreInformationForm(AdvanceSearchForm):
	searchCategory = (
		('storename', 'storename'), ('storeaddress', 'storeaddress'), ('storephonenumber', 'storephonenumber'),
		('cityname', 'cityname'), ('citystate', 'citystate'),
	)
	
	orderCategory = searchCategory + (('storeid', 'id'),)
	orderTypeCategory = (('ascending', 'ascending'), ('descending', 'descending'),)
	
	first_category = forms.ChoiceField(choices=searchCategory, required=False, initial='storename')
	second_category = forms.ChoiceField(choices=searchCategory, required=False, initial='storename')
	third_category = forms.ChoiceField(choices=searchCategory, required=False, initial='storename')
	fourth_category = forms.ChoiceField(choices=searchCategory, required=False, initial='storename')
	fifth_category = forms.ChoiceField(choices=searchCategory, required=False, initial='storename')
	
	order_category = forms.ChoiceField(choices=orderCategory, required=False, initial='id')
	order_type = forms.ChoiceField(choices=orderTypeCategory, required=False, initial='ascending')

class CustomerInformationForm(AdvanceSearchForm):	
	
	searchCategory = (
		('customerfirstname', 'firstname'), ('customerlastname', 'lastname'),  
		('customeraddress', 'address'), ('customeroccupation', 'occupation'),
	)
	
	orderCategory = searchCategory + (('customerdob', 'dob'), ('customerid', 'id'),)
	orderTypeCategory = (('ascending', 'ascending'), ('descending', 'descending'),)
	
	# ('customerdob', 'dob'),
	first_category = forms.ChoiceField(choices=searchCategory, required=False, initial='firstname')
	second_category = forms.ChoiceField(choices=searchCategory, required=False, initial='firstname')
	third_category = forms.ChoiceField(choices=searchCategory, required=False, initial='firstname')
	fourth_category = forms.ChoiceField(choices=searchCategory, required=False, initial='firstname')
	fifth_category = forms.ChoiceField(choices=searchCategory, required=False, initial='firstname')
	
	start_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',), required=False)
	end_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',), required=False)
	
	order_category = forms.ChoiceField(choices=orderCategory, required=False, initial='id')
	order_type = forms.ChoiceField(choices=orderTypeCategory, required=False, initial='ascending')
	
	# start_date = forms.DateField(required=False)
	# end_date = forms.DateField(required=False)
	

class UpdateProfileForm(forms.Form):
	cityidChoice = (
		('1', 'Alexandria'), ('2', 'Bendigo'), ('3', 'Brisbane'), ('4', 'Caloundra'), ('5', 'Cloverdale'), ('6', 'Coffs Harbour'), ('7', 'Cranbourne'), ('8', 'Darlinghurst'), ('9', 'East Brisbane'), ('10', 'Findon'),
		('11', 'Geelong'), ('12', 'Gold Coast'), ('13', 'Goulburn'), ('14', 'Hawthorne'), ('15', 'Harvey Bay'), ('16', 'Hobart'), ('17', 'Lane Cove'), ('18', 'Lavender Bay'), ('19', 'Malabar'), ('20', 'Matraville'),
		('21', 'Melbourne'), ('22', 'Melton'), ('23', 'Milsons Point'), ('24', 'Newcastle'), ('25', 'North Ryde'), ('26', 'North Sydney'), ('27', 'Perth'), ('28', 'Port Macquarie'), ('29', 'Rhodes'), ('30', 'Rockhampton'),
		('31', 'Seaford'), ('32', 'Sliverwater'), ('33', 'South Melbourne'), ('34', 'Springwood'), ('35', 'St. Leonards'), ('36', 'Sunbury'), ('37', 'Sydney'), ('38', 'Townsville'), ('39', 'Warrnambool'), ('40', 'Wollongong'),
	)
	email = forms.EmailField(label='Email   ', max_length=100, help_text='Update your email')
	firstName = forms.CharField(label='FirstName   ', max_length=50, help_text='Update your FirstName')
	lastName = forms.CharField(label='LastName   ', max_length=50, help_text='Update your LastName')
	phoneNumber = forms.CharField(label='Phone Number   ', max_length=11, help_text='Update your phone number')
	city = forms.ChoiceField(label='City   ', choices=cityidChoice, help_text='Choose your city')
	address = forms.CharField(label='Address   ', max_length=50, help_text='Update your living address')
	
class EmailVerification(forms.Form):
	email = forms.EmailField(label='Email   ', max_length=100, help_text='Input your registration email')

class SendEmailForm(forms.Form):
	file = forms.Field(label='file', widget=forms.FileInput, required=False)
	message = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}),
	                          initial="Replace with your content")
	subject = forms.CharField(label='Subject', max_length=50)

class UpdateEmailForm(forms.Form):
	email = forms.EmailField(label='Email', max_length=100, help_text='Replace your current email with new one')

class MISsearch(forms.Form):
	# predefinedOption = forms.IntegerField()
	groupBy = forms.IntegerField()
	# periodofTime = forms.IntegerField()

predefienedChoices=[('1','Both'),('2','Car Pickup'),('3','Car Return')]
periodofTimeChoices=[('1','Monthly'),('2','Quarterly'), ('3','Annually'), ('4','Month Over Year'), ('5','Quarter Over Year'), ( '6','Top 10 Cities (all cities)')]
wheelDriveChoices=[('1','FWD'),('2','RWD'),('3','4WD')]
transmissionChoices=[('1','Automatic'),('2','Manual')]
allCitiesChoice=[('1','All Cities')]
numberOfChoices=[('1','Sales'),('2','Different Makes'), ('3','Different Models')]
makemodelChoices=[('1', 'All'),('2','Make'),('3', 'Model')]

class MISForm(forms.Form):
	predOptions = forms.ChoiceField(
		required=False,
		#label = 'Predefined Options:',
		widget=forms.RadioSelect(),
		choices=predefienedChoices,
	)
	
	numberOf = forms.ChoiceField(
		required=False,
		widget=forms.RadioSelect(),
		choices=numberOfChoices,
	)

	
	periodTime = forms.ChoiceField(
		required=False,
		widget=forms.RadioSelect(),
		choices=periodofTimeChoices,
	)
	
	allCities = forms.BooleanField(required=False,)
	 
	selectCity = forms.ModelMultipleChoiceField(queryset=V_Cities.objects.all(),required=False)
	
	vWheelDrive = forms.BooleanField(required=False,)
	wheelDrive = forms.ChoiceField(
		required=False,
		widget=forms.RadioSelect(),
		choices=wheelDriveChoices,
	)
	
	vTransmission = forms.BooleanField(required=False,)
	transmission = forms.ChoiceField(
		required=False,
		widget=forms.RadioSelect(),
		choices=transmissionChoices,
	)

	vNoSeats = forms.BooleanField(required=False,)
	optNS1 = forms.CharField(required=False,)
	optNS2 = forms.CharField(required=False,)
	vTankCapacity = forms.BooleanField(required=False,)
	optTC1 = forms.CharField(required=False,)
	optTC2 = forms.CharField(required=False,)
	vPower= forms.BooleanField(required=False,)
	optPW1 = forms.CharField(required=False,)
	optPW2 = forms.CharField(required=False,)
	vEngineSize = forms.BooleanField(required=False,)
	optES1 = forms.CharField(required=False,)
	optES2 = forms.CharField(required=False,)
	vCarYear = forms.BooleanField(required=False,)
	optCY1 = forms.CharField(required=False,)
	optCY2 = forms.CharField(required=False,)
	vWheelBase = forms.BooleanField(required=False,)
	optWB1 = forms.CharField(required=False,)
	optWB2 = forms.CharField(required=False,)
	
	selectMake = forms.ModelMultipleChoiceField(queryset=V_VehicleMake.objects.all(),required=False)
	selectModel = forms.ModelMultipleChoiceField(queryset=V_VehicleModel.objects.all(),required=False)
	selectMakeModel = forms.ChoiceField(
		required=False,
		widget=forms.RadioSelect(),
		choices=makemodelChoices,
	)

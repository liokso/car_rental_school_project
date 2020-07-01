# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Citylist(models.Model):
    cityid = models.IntegerField(db_column='cityID', primary_key=True)  # Field name made lowercase.
    cityname = models.CharField(db_column='cityName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    citystate = models.CharField(db_column='cityState', max_length=5, blank=True, null=True)  # Field name made lowercase.
    citycountry = models.CharField(db_column='cityCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'citylist'


class Customer(models.Model):
    customerid = models.IntegerField(db_column='customerID', primary_key=True)  # Field name made lowercase.
    customerfirstname = models.CharField(db_column='customerFirstName', max_length=50)  # Field name made lowercase.
    customerlastname = models.CharField(db_column='customerLastName', max_length=50)  # Field name made lowercase.
    customerdob = models.DateField(db_column='customerDOB', blank=True, null=True)  # Field name made lowercase.
    customeraddress = models.CharField(db_column='customerAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customeroccupation = models.CharField(db_column='customerOccupation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customergender = models.CharField(db_column='customerGender', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class Customerphonenumber(models.Model):
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customerID')  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=13)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customerphonenumber'
        unique_together = (('customerid', 'phonenumber'),)


class Employee(models.Model):
    employeeid = models.AutoField(db_column='employeeID', primary_key=True)  # Field name made lowercase.
    employeefirstname = models.CharField(db_column='employeeFirstName', max_length=50)  # Field name made lowercase.
    employeelastname = models.CharField(db_column='employeeLastName', max_length=50)  # Field name made lowercase.
    employeedob = models.DateField(db_column='employeeDOB', blank=True, null=True)  # Field name made lowercase.
    employeeaddress = models.CharField(db_column='employeeAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    employeecityid = models.IntegerField(db_column='employeeCityID', blank=True, null=True)  # Field name made lowercase.
    employeeemail = models.CharField(db_column='employeeEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    employeephonenumber = models.IntegerField(db_column='employeePhoneNumber', blank=True, null=True)  # Field name made lowercase.
    roleid = models.ForeignKey('Employeerole', models.DO_NOTHING, db_column='roleID', blank=True, null=True)  # Field name made lowercase.
    employeeusername = models.CharField(db_column='employeeUsername', max_length=50, blank=True, null=True)  # Field name made lowercase.
    employeepassword = models.CharField(db_column='employeePassword', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class Employeerole(models.Model):
    roleid = models.AutoField(db_column='roleID', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='roleName', max_length=30)  # Field name made lowercase.
    roleaccesslevel = models.IntegerField(db_column='roleAccessLevel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employeerole'


class Salesorder(models.Model):
    orderid = models.IntegerField(db_column='orderID', primary_key=True)  # Field name made lowercase.
    createdate = models.DateField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    pickupdate = models.DateField(db_column='pickupDate', blank=True, null=True)  # Field name made lowercase.
    pickupstoreid = models.ForeignKey('Store', models.DO_NOTHING, db_column='pickupStoreID', blank=True, null=True)  # Field name made lowercase.
    returndate = models.DateField(db_column='returnDate', blank=True, null=True)  # Field name made lowercase.
    returnstoreid = models.ForeignKey('Store', models.DO_NOTHING, db_column='returnStoreID', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customerID', blank=True, null=True)  # Field name made lowercase.
    vehicleid = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='vehicleID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salesorder'


class Store(models.Model):
    storeid = models.IntegerField(db_column='storeID', primary_key=True)  # Field name made lowercase.
    storename = models.CharField(db_column='storeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    storeaddress = models.CharField(db_column='storeAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    storephonenumber = models.CharField(db_column='storePhoneNumber', max_length=13, blank=True, null=True)  # Field name made lowercase.
    storecityid = models.ForeignKey(Citylist, models.DO_NOTHING, db_column='storeCityID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store'


class Vehicle(models.Model):
    vehicleid = models.IntegerField(db_column='vehicleID', primary_key=True)  # Field name made lowercase.
    makename = models.CharField(db_column='makeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(max_length=50, blank=True, null=True)
    series = models.CharField(max_length=50, blank=True, null=True)
    seriesyear = models.IntegerField(db_column='seriesYear', blank=True, null=True)  # Field name made lowercase.
    pricenew = models.DecimalField(db_column='priceNew', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    enginesize = models.DecimalField(db_column='engineSize', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    fuelsystem = models.CharField(db_column='fuelSystem', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tankcapacity = models.DecimalField(db_column='tankCapacity', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    seatingcapacity = models.IntegerField(db_column='seatingCapacity', blank=True, null=True)  # Field name made lowercase.
    standardtransmission = models.CharField(db_column='standardTransmission', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bodytype = models.CharField(db_column='bodyType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wheeldrive = models.CharField(db_column='wheelDrive', max_length=3, blank=True, null=True)  # Field name made lowercase.
    wheelbase = models.DecimalField(db_column='wheelBase', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicle'

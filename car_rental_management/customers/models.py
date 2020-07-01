from django.db import models
from django.urls import reverse
# Create your models here.
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

    def get_absolute_url(self):
        return reverse('customers:detail', kwargs={'pk': self.vehicleid})

    class Meta:
        managed = False
        db_table = 'vehicle'

class V_CarpCitypMonth(models.Model):
	misCity = models.CharField(db_column='city',max_length=50,primary_key=True)
	misMake = models.CharField(db_column='make', max_length=50,blank=True, null=True)
	misModel = models.CharField(db_column='model', max_length=50,blank=True, null=True)
	misMonth = models.CharField(db_column='dateMonth', max_length=50,blank=True, null=True)
	misQuarter = models.IntegerField(db_column='dateQuarter',blank=True, null=True)
	misYear = models.IntegerField(db_column='dateYear',blank=True, null=True)
	misQuantity = models.IntegerField(db_column='quantity',blank=True, null=True)
	class Meta:
		managed = False
		unique_together = (('misCity','misMake', 'misModel', 'misMonth', 'misQuarter','misYear','misQuantity' ),)
		db_table = 'v_carpcitypmonth'
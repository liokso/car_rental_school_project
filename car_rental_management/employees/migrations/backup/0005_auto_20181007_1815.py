# Generated by Django 2.1 on 2018-10-07 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_auto_20181007_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employeeemailverify',
            field=models.CharField(db_column='employeeEmailVerify', default='0', max_length=40),
        ),
    ]
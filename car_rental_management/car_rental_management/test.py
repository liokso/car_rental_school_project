from car_rental_management.settings import *
from django.test.runner import DiscoverRunner
 
MIGRATION_MODULES = {
    'myapp': 'car_rental_management.apps.employees.test_migrations',
}
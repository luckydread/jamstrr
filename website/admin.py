from django.contrib import admin
from .models import Record

#Add record to admin page
admin.site.register(Record)
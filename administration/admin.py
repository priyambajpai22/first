from django.contrib import admin

# Register your models here.
from administration.models import Student,Fee,Content,Contact,Common

admin.site.register(Student)
admin.site.register(Fee)
admin.site.register(Contact)
admin.site.register(Content)
admin.site.register(Common)
from django.contrib import admin
from .models import Student, teacher, Contact

# Register your models here.
admin.site.register(Student)
admin.site.register(teacher)
admin.site.register(Contact)
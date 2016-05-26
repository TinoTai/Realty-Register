from django.contrib import admin

from main_app.models import Subject, RealtyObject, Request
from main_app.models import MainRight, Issue, SecondaryRight



# Register your models here.
admin.site.register(Subject)
admin.site.register(RealtyObject)
admin.site.register(Request)
admin.site.register(MainRight)
admin.site.register(Issue)
admin.site.register(SecondaryRight)
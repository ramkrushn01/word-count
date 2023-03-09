from django.contrib import admin
from wordapp.models import Contact,Savefile,Membership

# Register your models here.
admin.site.register([Contact,Savefile,Membership])
# admin.site.register(Savefile)
# admin.site.register(Savefile)

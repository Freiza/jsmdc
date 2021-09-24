from django.contrib import admin
from .models import User,Lead,JAdmin,Sandghat,LeadFile
# Register your models here.
from django.contrib import admin

admin.site.site_title = "JSMDC e-Lottery"
admin.site.site_header = "JSMDC e-Lottery"
admin.site.index_title = "JSMDC e-Lottery"

admin.site.register(User)
admin.site.register(JAdmin)
admin.site.register(Lead)
admin.site.register(Sandghat)
admin.site.register(LeadFile)
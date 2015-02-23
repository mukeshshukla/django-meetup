from django.contrib import admin

from models import Testing

class TestingAdmin(admin.ModelAdmin):
	list_display= (
	'username',
	'created_date',
	)

admin.site.register(Testing, TestingAdmin)

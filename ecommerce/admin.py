from django.contrib import admin
from ecommerce.models import Account ,Account_aff

# Register your models here.
class AccountModelAdmin(admin.ModelAdmin):
	list_display=["__unicode__","firstname","timestamp"]
	list_filter=["timestamp","updated"]
	search_fields=["firstname"]
	class Meta:
		model=Account
admin.site.register(Account,AccountModelAdmin)


class AccountModelAff(admin.ModelAdmin):
	list_display=["user","affliate_id","title","company","domain","dob"]
	# list_filter=["timestamp","updated"]
	# search_fields=["firstname"]
	class Meta:
		model=Account_aff
admin.site.register(Account_aff,AccountModelAff)
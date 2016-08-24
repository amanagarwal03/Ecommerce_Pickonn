from django.contrib import admin
from ecommerce.models import Account

# Register your models here.
class AccountModelAdmin(admin.ModelAdmin):
	list_display=["__unicode__","firstname","timestamp"]
	list_filter=["timestamp","updated"]
	search_fields=["firstname"]
	class Meta:
		model=Account
admin.site.register(Account,AccountModelAdmin)
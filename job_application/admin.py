from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email")
    list_filter = ("date","occupation")
    search_fields = ("first_name","last_name","occupation")
    readonly_fields = ("occupation",)
    ordering = ("first_name",)


admin.site.register(Form,FormAdmin)
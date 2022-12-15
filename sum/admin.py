from django.contrib import admin
from .models import patient, issue, detail
from import_export.admin import ImportExportModelAdmin
from sum.models import detail

# Register your models here.





admin.site.register(patient,ImportExportModelAdmin)


#@admin.register(patient)
#class patientAdmin(admin.ModelAdmin):
#   pass

@admin.register(issue)
class issueAdmin(admin.ModelAdmin):
    pass

@admin.register(detail)
class detailAdmin(admin.ModelAdmin):
    pass


'''class detailAdmin(admin.ModelAdmin):
    list_display=detail.displayfields
    search_fields=detail.searchablefields
    filter_fields=detail.filterfields'''

'''class detailAdmin(admin.ModelAdmin):
    list_display = ('patient', 'age', 'mobile_no')
    list_display_links = ('age', 'mobile_no')'''
class detailAdmin(admin.ModelAdmin):
    search_fields = ['gender']
    list_display = ('email', 'mobile_no', 'age','gender')
    #fields = (('first_name', 'last_name'), 'age', 'gender')
    exclude = ['age']
    list_filter = ['email']
    list_per_page = 5 

    




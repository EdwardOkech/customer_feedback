from django.contrib import admin
from cfback.models import *
from cfback.views import export_csv
from import_export import *
##from import_export.admin import ImportExportModelAdmin
##from import_export import fields, widgets

##class CustomerInline(admin.TabularInline):
##    model = Customer
##    extra = 1

##class FeedbackAdmin(ImportExportModelAdmin):
##    actions = ['export_csv']
    
##    fieldsets = (
##        (None, {'fields':('title','company','status')}),
##        )
##    inlines = (
##        CustomerInline,
##        )


##    def export_csv(modeladmin, request, queryset):
##        response = HttpResponse(content_type='text/csv')
##        response['Content-Disposition']  = 'attachement; filename=feedback.csv'
##        write = csv.write(response, csv.excel)
##
##        response.write(u'\ufeff'.encode('utf8'))
##        write.writerow([
##            smart_str(u"ID"),
##            smart_str(u"TITLE"),
##            smart_str(u"DATE_POSTED"),
##            smart_str(u"CUSTOMER"),
##            smart_str(u"COMPANY"),
##            smart_str(u"STATUS"),
##            ])
##        for obj in queryset:
##          write.writerow([
##               smart_str(obj.pk),
##               smart_str(obj.title),
##               smart_str(obj.date_posted),
##               smart_str(obj.customer),
##               smart_str(obj.company),
##               smart_str(obj.status),
##               ])
##          write.save(response)
##          return response
##          export_csv.short_description = u"Export CSV"

admin.site.register(City)
admin.site.register(Sector)
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Feedback)
admin.site.register(Faq)
admin.site.register(Team)


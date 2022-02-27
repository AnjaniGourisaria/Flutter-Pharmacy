from django.contrib import admin
from .models import Contacts
from .models import Consumer

admin.site.register(Contacts)

admin.site.disable_action('delete_selected')

@admin.action(description='Delete')
def is_deleted_true(modeladmin, request, queryset):
    queryset.update(is_deleted='True')

# @admin.action(description='Restore Soft')
# def is_deleted_false(modeladmin, request, queryset):
#     queryset.update(is_deleted='False')
  
class ConsumerModelAdmin(admin.ModelAdmin):
    list_display= ('id','user','phone','city','state','zipcode','station','address','email','publish_date')
    list_display_links = ('id','user','phone','city','state','zipcode','station','address','email','publish_date')
    list_filter = ('publish_date','city','state','is_deleted')
    save_on_top = True
    list_per_page = 20
    search_fields = ('foreignkeyfield__user',)
    save_on_top = True
    list_per_page = 20
    actions = [is_deleted_true]#,is_deleted_false]
admin.site.register(Consumer,ConsumerModelAdmin)


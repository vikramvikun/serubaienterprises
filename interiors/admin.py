from django.contrib import admin
from .models import index_table,services_table,works_table,contact_table,subservice,works_done

admin.site.register(index_table)
admin.site.register(services_table)
admin.site.register(works_table)
admin.site.register(contact_table)
admin.site.register(subservice)
admin.site.register(works_done)

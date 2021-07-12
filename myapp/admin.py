from django.contrib import admin
from myapp.models  import Details

# Register your models here.


admin.site.register(Details)
admin.site.site_header = "Keshav-e-World Admin"
admin.site.index_title = "Admin"
admin.site.site_title = "Keshav-e-World"
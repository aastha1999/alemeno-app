from django.contrib import admin
from assignment.models import Kid, Image

# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Kid)
admin.site.register(Image)
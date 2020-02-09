from django.contrib import admin
from .models import Rebus


class RebusAdmin(admin.ModelAdmin):
    model = Rebus


admin.site.register(Rebus, RebusAdmin)


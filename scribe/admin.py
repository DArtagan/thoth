from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from scribe.models import Email, Template, Header

class ProperDisplay(GuardedModelAdmin):
    list_display = ('__unicode__',)

admin.site.register(Email, ProperDisplay)
admin.site.register(Template, ProperDisplay)
admin.site.register(Header, ProperDisplay)

from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from scribe.models import Email, Template, Header

admin.site.register(Email, GuardedModelAdmin)
admin.site.register(Template, GuardedModelAdmin)
admin.site.register(Header, GuardedModelAdmin)

from django.contrib import admin
from .models import Project  # The dot (.) is crucial!

admin.site.register(Project)

from .models import Project, ContactMessage

admin.site.register(ContactMessage)
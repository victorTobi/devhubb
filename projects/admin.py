from django.contrib import admin

# Register your models here.
from .models import Project, Review, Tag


#models from "projects/models.py" are registered here this way
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)
from django.contrib import admin
from features.models import User, Category, CategoryData

admin.site.register(User)
admin.site.register(Category)
admin.site.register(CategoryData)
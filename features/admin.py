from django.contrib import admin
from features.models import User, Category, CategoryData, Tansaction, Parking, NumberPlate

admin.site.register(User)
admin.site.register(Category)
admin.site.register(CategoryData)
admin.site.register(Parking)
admin.site.register(Tansaction)
admin.site.register(NumberPlate)
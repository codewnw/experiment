from django.contrib import admin
from item.models import Category, SubCategory, Item

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Item)

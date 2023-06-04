from django.contrib import admin
from .models import Product, Photo, Tag, Category

class PhotoInline(admin.StackedInline):
    model = Photo

class TagInline(admin.TabularInline):
    model = Tag.product_set.through

class CategoryInline(admin.TabularInline):
    model = Category.product_set.through

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, TagInline, CategoryInline]

admin.site.register(Photo)
admin.site.register(Tag)
admin.site.register(Category)
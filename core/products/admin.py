from django.contrib import admin
from .models import Product, Photo, Tag, Category, Status, Currency

class PhotoInline(admin.StackedInline):
    model = Photo

class TagInline(admin.TabularInline):
    model = Tag.product_set.through

class CategoryInline(admin.TabularInline):
    model = Category.product_set.through

class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, TagInline, CategoryInline]

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'singular_name', 'plural_name', 'symbol', 'std_int')

admin.site.register(Photo)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Currency, CurrencyAdmin)
from django.contrib import admin
from .models import Category, Product, ProductImage, Cart, CartItem, Order, OrderItem

class ProductImageInline(admin.TabularInline):
    model = ProductImage      
    extra = 4                 
    fields = ['image']        
@admin.register(Product)    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available']  
    inlines = [ProductImageInline] 

class SubCategoryInline(admin.TabularInline):
    model = Category
    fields = ['name', 'slug']
    extra = 3
    fk_name = 'parent'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']  
    list_filter = ['parent']           
    search_fields = ['name']
    inlines = [SubCategoryInline]


admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
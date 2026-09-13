from django.contrib import admin
from django.contrib import admin
from .models import Order, OrderDetail


class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_ordered', 'total_price', 'created_at')
    list_filter = ('is_ordered',)
    inlines = [OrderDetailInline]


# Register your models here.

from django.db import models
from django.conf import settings
from django.db import models


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders', verbose_name="کاربر")
    is_ordered = models.BooleanField(default=False, verbose_name="نهایی شده؟")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "سفارش"
        verbose_name_plural = "سفارشات"

    def __str__(self):
        return f"سفارش #{self.id} - {self.user}"

    @property
    def total_price(self):
        return sum(detail.subtotal for detail in self.details.all())

    @property
    def total_count(self):
        return sum(detail.count for detail in self.details.all())


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details', verbose_name="سفارش")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name="محصول")
    count = models.PositiveIntegerField(default=1, verbose_name="تعداد")

    class Meta:
        verbose_name = "ردیف سفارش"
        verbose_name_plural = "ردیف‌های سفارش"

    def __str__(self):
        return f"{self.product.title} × {self.count}"

    @property
    def subtotal(self):
        return self.product.price * self.count

# Create your models here.

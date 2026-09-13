from django.db import models
from django.conf import settings
from django.db import models


class WishlistItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="کاربر")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name="محصول")
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ افزودن")

    class Meta:
        unique_together = ('user', 'product')
        verbose_name = "آیتم علاقه‌مندی"
        verbose_name_plural = "علاقه‌مندی‌ها"

    def __str__(self):
        return f"{self.user} - {self.product.title}"


# Create your models here.

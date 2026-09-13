from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="نام دسته‌بندی")
    slug = models.SlugField(max_length=170, unique=True, verbose_name="اسلاگ")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='products', verbose_name="دسته‌بندی"
    )
    title = models.CharField(max_length=250, verbose_name="عنوان محصول")
    slug = models.SlugField(max_length=270, unique=True, verbose_name="اسلاگ")
    sku = models.CharField(max_length=50, blank=True, verbose_name="کد محصول")
    price = models.PositiveIntegerField(verbose_name="قیمت (تومان)")
    old_price = models.PositiveIntegerField(null=True, blank=True, verbose_name="قیمت قبل از تخفیف")
    short_description = models.TextField(blank=True, verbose_name="توضیح کوتاه")
    description = models.TextField(blank=True, verbose_name="توضیحات کامل")
    is_available = models.BooleanField(default=True, verbose_name="موجود است؟")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    @property
    def main_image(self):
        first = self.images.first()
        return first.image if first else None

    @property
    def review_count(self):
        return self.reviews.count()

    @property
    def rating_percent(self):
        """میانگین امتیازها به‌صورت درصد (برای نمایش نوار ستاره‌ای)"""
        reviews = self.reviews.all()
        if not reviews:
            return 0
        avg = sum(r.rating for r in reviews) / len(reviews)
        return int(avg * 20)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name="محصول")
    image = models.ImageField(upload_to='products/', verbose_name="تصویر")
    order = models.PositiveIntegerField(default=0, verbose_name="ترتیب")

    class Meta:
        ordering = ['order']
        verbose_name = "تصویر محصول"
        verbose_name_plural = "تصاویر محصول"

    def __str__(self):
        return f"تصویر {self.product.title}"


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name="محصول")
    name = models.CharField(max_length=100, verbose_name="نام")
    email = models.EmailField(blank=True, verbose_name="ایمیل")
    rating = models.PositiveSmallIntegerField(default=5, verbose_name="امتیاز (1 تا 5)")
    comment = models.TextField(verbose_name="متن نظر")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "نظر محصول"
        verbose_name_plural = "نظرات محصول"

    def __str__(self):
        return f"نظر {self.name} برای {self.product.title}"

    @property
    def rating_percent(self):
        return self.rating * 20

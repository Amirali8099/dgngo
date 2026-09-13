# from django.db import models
# from django.db import models
#
#
# class ContactMessage(models.Model):
#     username = models.CharField(max_length=100, verbose_name="نام")
#     email = models.EmailField(verbose_name="ایمیل")
#     message = models.TextField(verbose_name="پیام")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")
#
#     class Meta:
#         ordering = ['-created_at']
#         verbose_name = "پیام تماس با ما"
#         verbose_name_plural = "پیام‌های تماس با ما"
#
#     def __str__(self):
#         return f"پیام از {self.username}"
#
#
# # Create your models here.

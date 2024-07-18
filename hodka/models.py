from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.

# صفحه اسلایدر اولی
class slider(models.Model):
    image = models.ImageField(help_text="تصویر", verbose_name="تصویر اسلایدرها", upload_to="sliders/")
    title = models.CharField(help_text="موضوع",max_length=50)
    content = models.CharField(help_text="متن",max_length=225)
    active = models.BooleanField(help_text="نمایش داده شود؟",default=False)

# مدرعامل
class CEO(models.Model):
    avatar = models.ImageField(help_text="تصویر شخص ", upload_to="ceo/")
    name = models.CharField(help_text=" نام و نام خانوادگی", max_length=100)
    role = models.CharField(help_text="نقش در کارگاه", max_length=100)
    descriptions = models.CharField(help_text="توضیحات", max_length=225)
    telegram = models.URLField(help_text="آیدی تلگرام",)
    phone = models.DecimalField(help_text="شماره موبایل", max_digits=11, decimal_places=10)

# رضایت ها
class Satisfaction(models.Model):
    image = models.ImageField(help_text="تصویر", upload_to="media/defaults/male_user.png")
    content = models.CharField(help_text="متن", max_length=225)
    name = models.CharField(help_text="نام", max_length=50 , default="")

# تماس با ما
class contactUs(models.Model):
    name = models.CharField(help_text="نام و نام خانوادگی", max_length=50)
    email = models.EmailField(help_text="ایمیل", max_length=100)
    message = models.CharField(help_text="متن", max_length=225)
    created_time = jmodels.jDateTimeField(help_text="تاریخ ایجاد", auto_now_add=True)


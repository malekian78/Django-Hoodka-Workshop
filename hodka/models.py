from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.

# صفحه اسلایدر اولی
class slider(models.Model):
    image = models.ImageField(verbose_name="تصویر اسلایدرها", upload_to="sliders/")
    title = models.CharField(verbose_name="موضوع",max_length=50)
    content = models.TextField(verbose_name="متن",max_length=225)
    active = models.BooleanField(verbose_name="نمایش داده شود؟",default=False)
    
    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدر"

# مدرعامل
class CEO(models.Model):
    avatar = models.ImageField(verbose_name="تصویر شخص ", upload_to="ceo/", default="defaults\male_user.png")
    name = models.CharField(verbose_name=" نام و نام خانوادگی", max_length=100)
    role = models.CharField(verbose_name="نقش در کارگاه", max_length=100)
    descriptions = models.TextField(verbose_name="توضیحات", max_length=225)
    # telegram = models.URLField(verbose_name="آیدی تلگرام",)
    phone = models.CharField(verbose_name="شماره موبایل", max_length=11)
    
    class Meta:
        verbose_name = "مدیران"
        verbose_name_plural = "مدیران"

# رضایت ها
class Satisfaction(models.Model):
    name = models.CharField(verbose_name="نام و نام خانوادگی", max_length=50 , help_text= "برای تجربه کاربری بهتر حداقل ۳ رکورد ایجاد کنید")
    content = models.TextField(verbose_name="متن", max_length=225)
    image = models.ImageField(verbose_name="تصویر", upload_to="satisfaction/", default="defaults/male_user.png")
    class Meta:
        verbose_name = "رضایتمندی"
        verbose_name_plural = "رضایتمندی"
# تماس با ما
class contactUs(models.Model):
    name = models.CharField(verbose_name="نام و نام خانوادگی", max_length=50)
    email = models.EmailField(verbose_name="ایمیل", max_length=100)
    message = models.CharField(verbose_name="متن", max_length=225)
    created_time = jmodels.jDateTimeField(verbose_name="تاریخ ایجاد", auto_now_add=True)
    class Meta:
        verbose_name = "پیغام ها"
        verbose_name_plural = "پیغام ها"

class extraData(models.Model):
    active = models.BooleanField(verbose_name="نمایش داده شود؟")
    YearofExperience = models.PositiveIntegerField(verbose_name="چند سال تجربه؟")
    NumberofEngineers = models.PositiveIntegerField(verbose_name="تعداد کارمندها")
    Numberofsells = models.PositiveIntegerField(verbose_name="تعداد محصولات فروش رفته")
    NumberofProduct = models.PositiveIntegerField(verbose_name="میزان تولید در روز")
    backGroundImage1 = models.ImageField(verbose_name="تصویر بک گراند۱", upload_to="extraData/")
    backGroundImage2 = models.ImageField(verbose_name="تصویر بک گراند۲", upload_to="extraData/")
    aboutUsContent = models.TextField(verbose_name="متن درباره ما", default='SOME STRING')
    logo = models.ImageField(verbose_name="لوگو", upload_to="logo/")
    class Meta:
        verbose_name = "داده های دیگر"
        verbose_name_plural = "داده های دیگر"

class Product(models.Model):
    title = models.CharField(verbose_name="نام محصول" ,max_length=100)
    image = models.ImageField(verbose_name="تصویر محصول", upload_to="products/")
    snipetContent = models.TextField(verbose_name="توضیحات محصول")
    # createdTime = jmodels.jDateField(verbose_name="سال ساخت (اختیاری)", null=True, blank=True)
    active = models.BooleanField(verbose_name="نمایش داده شود؟")
    class Meta:
        verbose_name = "محصولات"
        verbose_name_plural = "محصولات"
    
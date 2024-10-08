# Generated by Django 4.2 on 2024-07-18 08:17

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ("hodka", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="extraData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("active", models.BooleanField()),
                (
                    "YearofExperience",
                    models.PositiveIntegerField(verbose_name="میزان سابقه ( به سال)"),
                ),
                (
                    "NumberofEngineers",
                    models.PositiveIntegerField(verbose_name="تعداد کارمندها"),
                ),
                (
                    "Numberofsells",
                    models.PositiveIntegerField(verbose_name="تعداد محصولات فروش رفته"),
                ),
                (
                    "NumberofProduct",
                    models.PositiveIntegerField(
                        verbose_name="تعداد محصولات تولید شده در روز"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="ceo",
            name="avatar",
            field=models.ImageField(upload_to="ceo/", verbose_name="تصویر شخص "),
        ),
        migrations.AlterField(
            model_name="ceo",
            name="descriptions",
            field=models.CharField(max_length=225, verbose_name="توضیحات"),
        ),
        migrations.AlterField(
            model_name="ceo",
            name="name",
            field=models.CharField(max_length=100, verbose_name=" نام و نام خانوادگی"),
        ),
        migrations.AlterField(
            model_name="ceo",
            name="phone",
            field=models.DecimalField(
                decimal_places=10, max_digits=11, verbose_name="شماره موبایل"
            ),
        ),
        migrations.AlterField(
            model_name="ceo",
            name="role",
            field=models.CharField(max_length=100, verbose_name="نقش در کارگاه"),
        ),
        migrations.AlterField(
            model_name="ceo",
            name="telegram",
            field=models.URLField(verbose_name="آیدی تلگرام"),
        ),
        migrations.AlterField(
            model_name="contactus",
            name="created_time",
            field=django_jalali.db.models.jDateTimeField(
                auto_now_add=True, verbose_name="تاریخ ایجاد"
            ),
        ),
        migrations.AlterField(
            model_name="contactus",
            name="email",
            field=models.EmailField(max_length=100, verbose_name="ایمیل"),
        ),
        migrations.AlterField(
            model_name="contactus",
            name="message",
            field=models.CharField(max_length=225, verbose_name="متن"),
        ),
        migrations.AlterField(
            model_name="contactus",
            name="name",
            field=models.CharField(max_length=50, verbose_name="نام و نام خانوادگی"),
        ),
        migrations.AlterField(
            model_name="satisfaction",
            name="content",
            field=models.CharField(max_length=225, verbose_name="متن"),
        ),
        migrations.AlterField(
            model_name="satisfaction",
            name="image",
            field=models.ImageField(
                upload_to="media/defaults/male_user.png", verbose_name="تصویر"
            ),
        ),
        migrations.AlterField(
            model_name="satisfaction",
            name="name",
            field=models.CharField(default="", max_length=50, verbose_name="نام"),
        ),
        migrations.AlterField(
            model_name="slider",
            name="active",
            field=models.BooleanField(default=False, verbose_name="نمایش داده شود؟"),
        ),
        migrations.AlterField(
            model_name="slider",
            name="content",
            field=models.TextField(max_length=225, verbose_name="متن"),
        ),
        migrations.AlterField(
            model_name="slider",
            name="image",
            field=models.ImageField(
                upload_to="sliders/", verbose_name="تصویر اسلایدرها"
            ),
        ),
        migrations.AlterField(
            model_name="slider",
            name="title",
            field=models.CharField(max_length=50, verbose_name="تست"),
        ),
    ]

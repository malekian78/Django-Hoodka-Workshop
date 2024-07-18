# Generated by Django 4.2 on 2024-07-18 07:00

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CEO",
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
                ("avatar", models.ImageField(help_text="تصویر شخص ", upload_to="ceo/")),
                (
                    "name",
                    models.CharField(help_text=" نام و نام خانوادگی", max_length=100),
                ),
                ("role", models.CharField(help_text="نقش در کارگاه", max_length=100)),
                ("descriptions", models.CharField(help_text="توضیحات", max_length=225)),
                ("telegram", models.URLField(help_text="آیدی تلگرام")),
                (
                    "phone",
                    models.DecimalField(
                        decimal_places=10, help_text="شماره موبایل", max_digits=11
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="contactUs",
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
                (
                    "name",
                    models.CharField(help_text="نام و نام خانوادگی", max_length=50),
                ),
                ("email", models.EmailField(help_text="ایمیل", max_length=100)),
                ("message", models.CharField(help_text="متن", max_length=225)),
                (
                    "created_time",
                    django_jalali.db.models.jDateTimeField(
                        auto_now_add=True, help_text="تاریخ ایجاد"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Satisfaction",
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
                (
                    "image",
                    models.ImageField(
                        help_text="تصویر", upload_to="media/defaults/male_user.png"
                    ),
                ),
                ("content", models.CharField(help_text="متن", max_length=225)),
                ("name", models.CharField(default="", help_text="نام", max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="slider",
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
                (
                    "image",
                    models.ImageField(
                        help_text="تصویر",
                        upload_to="sliders/",
                        verbose_name="تصویر اسلایدرها",
                    ),
                ),
                ("title", models.CharField(help_text="موضوع", max_length=50)),
                ("content", models.CharField(help_text="متن", max_length=225)),
                (
                    "active",
                    models.BooleanField(default=False, help_text="نمایش داده شود؟"),
                ),
            ],
        ),
    ]

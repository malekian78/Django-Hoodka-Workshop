# Generated by Django 4.2 on 2024-07-19 04:54

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ("hodka", "0005_alter_ceo_descriptions_alter_satisfaction_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=100, verbose_name="نام محصول")),
                (
                    "image",
                    models.ImageField(
                        upload_to="products/", verbose_name="تصویر محصول"
                    ),
                ),
                ("snipetContent", models.TextField(verbose_name="توضیحات محصول")),
                (
                    "createdTime",
                    django_jalali.db.models.jDateField(
                        verbose_name="سال ساخت (اختیاری)"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="ceo",
            name="avatar",
            field=models.ImageField(
                default="defaults\\male_user.png",
                upload_to="ceo/",
                verbose_name="تصویر شخص ",
            ),
        ),
        migrations.AlterField(
            model_name="satisfaction",
            name="content",
            field=models.TextField(max_length=225, verbose_name="متن"),
        ),
        migrations.AlterField(
            model_name="satisfaction",
            name="name",
            field=models.CharField(
                help_text="برای تجربه کاربری بهتر حداقل ۳ رکورد ایجاد کنید",
                max_length=50,
                verbose_name="نام و نام خانوادگی",
            ),
        ),
    ]

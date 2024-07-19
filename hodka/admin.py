from django.contrib import admin
from .models import slider, CEO, Satisfaction, contactUs, extraData, Product


@admin.register(slider)
class sliderAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "active", "content")
    list_display_links = ("id", "title")
    list_filter = ("title", "active", )
    search_fields = ("title", "content")
    ordering = ("title", )

@admin.register(CEO)
class CEOAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "role", "descriptions",)
    list_display_links = ("id", "name")
    list_filter = ("name", "role", )
    search_fields = ("name", "descriptions", "role",)
    ordering = ("role", )

@admin.register(Satisfaction)
class SatisfactionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "content",)
    list_display_links = ("id", "name")
    list_filter = ("name", )
    search_fields = ("name", "descriptions", "role",)
    ordering = ("name", )

@admin.register(contactUs)
class contactUsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "message", "created_time")
    list_display_links = ("id", "name", "email",)
    list_filter = ("name", "created_time", )
    search_fields = ("name", "message",)
    ordering = ("name", )

@admin.register(extraData)
class extraDataAdmin(admin.ModelAdmin):
    list_display = ("id", "active", "YearofExperience", "NumberofEngineers", "aboutUsContent")
    list_display_links = ("id", "active", "YearofExperience", "NumberofEngineers", "aboutUsContent")
    list_filter = ("active", )
    search_fields = ("aboutUsContent", )
    ordering = ("active", )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "snipetContent", )
    list_display_links = ("id", "title", "snipetContent", )
    list_filter = ("title", )
    search_fields = ("title", "snipetContent")
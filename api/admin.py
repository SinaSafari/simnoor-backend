from django.contrib import admin
from api.models import Contact, News, Product


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'en_title', 'fa_title', 'created_at',)
    list_display_links = ('created_at', 'fa_title',)
    search_fields = ('en_title', 'fa_title', )
    list_filter = ('created_at',)
    list_per_page = 10


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'en_title', 'fa_title', 'created_at', 'featured')
    list_display_links = ('en_title', 'fa_title',)
    list_editable = ('featured',)
    list_filter = ('featured',)
    search_fields = ('en_title', 'fa_title', )
    list_per_page = 10


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'sender_name',
                    'is_responsed', 'created_at',)
    list_display_links = ('subject',)
    search_fields = ('subject', 'sender_name', )
    list_filter = ('sender_name', 'is_responsed',)
    list_editable = ('is_responsed',)
    list_per_page = 10


admin.site.register(Contact, ContactAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Product, ProductAdmin)

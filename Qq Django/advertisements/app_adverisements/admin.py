from django.contrib import admin
from .models import Advertisement

# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'auction', 'updated_date']

    list_filter = ['auction', 'created_at']
    actions = ['make_auction_false', 'make_auction_true']

    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description'),
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            # "'classes': ['collapse'] <-- hide/show
        }),
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_true(self, request, queryset):
        queryset.update(auction=True)



admin.site.register(Advertisement, AdvertisementAdmin)


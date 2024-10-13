from django.contrib import admin
from .models import NormalSkin, OilySkin, DrySkin, CombinationSkin, Recommendations, HealthcareRecommendations, body_Recommendations

class NormalSkinAdmin(admin.ModelAdmin):
    list_display = ('facewash_name', 'moisturizer_name', 'serum_name', 'sunscreen_name','face_image','face_link')
    search_fields = ('facewash_name', 'moisturizer_name', 'serum_name', 'sunscreen_name','face_image','face_link')

class OilySkinAdmin(admin.ModelAdmin):
    list_display = ('facewash_name', 'moisturizer_name', 'serum_name', 'sunscreen_name','face_image','face_link')
    search_fields = ('facewash_name', 'moisturizer_name', 'serum_name', 'sunscreen_name','face_image','face_link')

class DrySkinAdmin(admin.ModelAdmin):
    list_display = ('facewash_name', 'moisturizer_name', 'serum_name', 'sunscreen_name','face_image','face_link')
    search_fields = ('facewash_name', 'moisturizer_name', 'serum_name', 'sunscreen_name','face_image','face_link')

class CombinationSkinAdmin(admin.ModelAdmin):
    list_display = ('facewash_name', 'moisturizer_name', 'serum_name', 'sunscreen_name','face_image','face_link')
    search_fields = ('facewash_name', 'moisturizer_name', 'serum_name', 'sunscreen_name','face_image','face_link')

class RecommendationsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_image_url', 'purchase_link')
    search_fields = ('product_name',)

class HealthcareRecommendationsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_image_url', 'purchase_link')
    search_fields = ('product_name', 'category')

class body_RecommendationsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_image_url', 'purchase_link')
    search_fields = ('product_name',)


# Register your models here.
admin.site.register(NormalSkin, NormalSkinAdmin)
admin.site.register(OilySkin, OilySkinAdmin)
admin.site.register(DrySkin, DrySkinAdmin)
admin.site.register(CombinationSkin, CombinationSkinAdmin)
admin.site.register(Recommendations, RecommendationsAdmin)
admin.site.register(HealthcareRecommendations, HealthcareRecommendationsAdmin)
admin.site.register(body_Recommendations, body_RecommendationsAdmin)


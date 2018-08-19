from django.contrib import admin
from product.models import *
# Register your models here.
class ProductDetailAdmin(admin.ModelAdmin):
	list_display= ["id","name","quantity","brand","price","link","modified","created"]


admin.site.register(ProductDetail, ProductDetailAdmin)

class ProductNameAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "barcode" ]

admin.site.register(ProductName, ProductNameAdmin)

class CategoryDetailAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "categoryname" ]

admin.site.register(CategoryDetail,CategoryDetailAdmin)

class VideoDetailAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "videolink" ]

admin.site.register(VideoDetail,VideoDetailAdmin)


class ImageDetailAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "imagelink" ]

admin.site.register(ImageDetail,ImageDetailAdmin)

class NewsDetailAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "newslink","news" ]

admin.site.register(NewsDetail,NewsDetailAdmin)


class AllergyDetailAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "allergy" ]

admin.site.register(AllergyDetail,AllergyDetailAdmin)

class UserReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "review" ]

admin.site.register(UserReview,UserReviewAdmin)

class ExpertReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "expertreview" ]

admin.site.register(ExpertReview,ExpertReviewAdmin)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "ingredientname","ingredientvalue" ]

admin.site.register(Ingredient,IngredientAdmin)

class NutritionAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "fat","protein","carbohydrate","salt","other" ]

admin.site.register(NutritionValues,NutritionAdmin)








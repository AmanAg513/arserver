from __future__ import unicode_literals

from django.db import models

# Create your models here.


	

class ProductName(models.Model):
	name = models.CharField(max_length=120,blank=False,null=False)
	barcode = models.IntegerField(blank=False,null=False)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return str(self.name)
	
class ProductDetail(models.Model):
	
	name = models.ForeignKey(ProductName)
	quantity = models.CharField(max_length=120,blank=True,null=True)
	brand = models.CharField(max_length=120,blank=True,null=True)
	price = models.IntegerField(blank=True,null=True)
	link = models.CharField(max_length=120,blank=True,null=True)
	#image=models.ImageField(upload_to='category/',default="/media/category/default.png")
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

class CategoryDetail(models.Model):
	name = models.ForeignKey(ProductName)
	categoryname = models.CharField(max_length=120,blank=True,null=True)


class VideoDetail(models.Model):
	name = models.ForeignKey(ProductName)
	videolink = models.CharField(max_length=120,blank=True,null=True)

class ImageDetail(models.Model):
	name = models.ForeignKey(ProductName)
	imagelink = models.CharField(max_length=120,blank=True,null=True)

class NewsDetail(models.Model):
	name = models.ForeignKey(ProductName)
	newslink = models.CharField(max_length=120,blank=True,null=True)
	news = models.CharField(max_length=700,blank=True,null=True)

class AllergyDetail(models.Model):
	name = models.ForeignKey(ProductName)
	allergy= models.CharField(max_length=120,blank=True,null=True)
   
class UserReview(models.Model):
	name = models.ForeignKey(ProductName)
	review= models.CharField(max_length=1000,blank=True,null=True)

class ExpertReview(models.Model):
	name = models.ForeignKey(ProductName)
	expertreview= models.CharField(max_length=1000,blank=True,null=True)

class Ingredient(models.Model):
	name = models.ForeignKey(ProductName)
	ingredientname= models.CharField(max_length=120,blank=True,null=True)
	ingredientvalue= models.CharField(max_length=120,blank=True,null=True)

class NutritionValues(models.Model):
	name = models.ForeignKey(ProductName)
	fat= models.CharField(max_length=1000,blank=True,null=True)
	salt= models.CharField(max_length=1000,blank=True,null=True)
	protein= models.CharField(max_length=1000,blank=True,null=True)
	carbohydrate= models.CharField(max_length=1000,blank=True,null=True)
	energy= models.CharField(max_length=1000,blank=True,null=True)
	other=models.CharField(max_length=1000,blank=True,null=True)
	







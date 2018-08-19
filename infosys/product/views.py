from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
# Create your views here.

@csrf_exempt
def getdata(request):
	
	response={}
	try:
		name = request.GET.get('name')
		print name
		name1 = ProductName.objects.get(name=name)
		print name1.name
		print name1.barcode
		product_detail_instance = ProductDetail.objects.get(name=name1)
		response['name'] = name
		print name
		response['quantity'] =product_detail_instance.quantity
		response['brand'] = product_detail_instance.brand
		response['price'] = product_detail_instance.price
		response['link'] = product_detail_instance.link
		category_instance = CategoryDetail.objects.get(name=name1)
		response['category'] =category_instance.categoryname
		video_instance = VideoDetail.objects.get(name=name1)
		response['videolink'] =video_instance.videolink
		image_instance = ImageDetail.objects.get(name=name1)
		response['imagelink'] =image_instance.imagelink
		allergy_instance = AllergyDetail.objects.get(name=name1)
		response['allergy'] =allergy_instance.allergy
		userreview_instance = UserReview.objects.get(name=name1)
		print userreview_instance.review
		response['user_review'] =userreview_instance.review
		ingredient_instance = Ingredient.objects.get(name=name1)
		response['ingredient'] =ingredient_instance.ingredientname
		expert_instance = ExpertReview.objects.get(name=name1)
		response['expert_review'] =expert_instance.expertreview
		nutrition_instance = NutritionValues.objects.get(name=name1)
		response['fat'] =nutrition_instance.fat
		response['cholestrol'] = nutrition_instance.salt
		response['protein'] = nutrition_instance.protein
		response['carbohydrate'] = nutrition_instance.carbohydrate
		response['energy'] = nutrition_instance.energy
		response['success'] = True
		response['message'] = Done
	except Exception as e:
		print e
		response['success'] = False
		response['message'] = "Not able to search now"
	print response
	return JsonResponse(response)

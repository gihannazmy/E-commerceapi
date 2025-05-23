from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from product.filters import ProductFilter
from .models import *
from .serializers import ProductSerializer
from rest_framework import status
from django.db.models import Avg
# Create your views here.
@api_view(['GET'])
def get_all_products(request):
    # products = Product.objects.all()
    filterset = ProductFilter(request.GET,queryset=Product.objects.all().order_by('id'))
    serializer = ProductSerializer(filterset.qs, many=True)
    return Response({"products":serializer.data})


@api_view(['GET'])
def get_by_id_product(request,pk):
   products = get_object_or_404(Product, id=pk)
   serializer = ProductSerializer(products, many=False)
   return Response({"products":serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_product(request):
    data = request.data
    serializer = ProductSerializer(data = data)
    if serializer.is_valid():
        product = Product.object.create(**data, User=request.user)
        res = ProductSerializer(product,many=False)
        return Response({"product":res.data})
    else:
        return Response(serializer.errors)
    


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product(request,pk):
    product = get_object_or_404(Product,id=pk)
    if product.user != request.user:
        return Response({"error":"you can not update this product"},status=status.HTTP_403_FORBIDDEN)
    product.name = request.data['name']
    product.description = request.data['description']
    product.price = request.data['price']
    product.brand = request.data['brand']
    product.category = request.data['category']
    product.rating = request.data['rating']
    product.save()

    serializer = ProductSerializer(product, many=False)

    return Response({"product":serializer.data})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request,pk):
    product = get_object_or_404(Product,id=pk)
    if product.user != request.user:
        return Response({"error":"you can not update this product"},status=status.HTTP_403_FORBIDDEN)

    product.delete()


    return Response({"details":"Deletion is odne"}, status.HTTP_200_OK)

# Reviews Views

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_reveiw(request,pk):
    user = request.user
    product = get_object_or_404(Product,id=pk)
    data = request.data
    review = product.reviews.filter(user=user)
   
    if data['rating'] < 0 or data['rating'] > 5 :
        return Response({"error":"Please select between 1 to 5 only"}, status=status.HTTP_400_BAD_REQUEST)
    elif review.exists():
        new_reveiw = {"rating":data["rating"], "comment":data["comment"]}
        review.update(**new_reveiw)

        rating = product.reviews.aggregate(avg_ratings = Avg('rating'))
        product.ratings = rating['avg_ratings']
        product.save()
        return Response({"details":"Product review updated"})
    else:
        Review.objects.create(
            user=user,
            product=product,
            rating=data['rating'],
            comment = data['comment']
        )
        
        rating = product.reviews.aggregate(avg_ratings = Avg('rating'))
        product.ratings = rating['avg_ratings']
        product.save()
        return Response({"details":"Product review updated"})



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_review(request,pk):
    user = request.user
    product = get_object_or_404(Product,id=pk)
    data = request.data
    review = product.reviews.filter(user=user)
    if review.exists():
       review.delete()
       rating  = product.reviews.aggregate(avg_ratings = Avg('rating'))
       if rating['avg_ratings '] is None:
            rating['avg_ratings '] = 0
            product.ratings = rating['avg_ratings ']
            product.save()
            return Response({"details":"Deletion is odne"}, status.HTTP_200_OK)

    else:
        return Response({"error":"review is not found"}, status.HTTP_404_NOT_FOUND)
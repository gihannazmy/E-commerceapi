import json
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from .models import *
from .serializers import *
from rest_framework import status
from django.db.models import Avg




# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders,many=True)
    return  Response({"orders":serializer.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order(request,pk):
    order = get_object_or_404(Order,id=pk)
    serializer = OrderSerializer(order,many=False)
    return  Response({"order":serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_order(request):
    user = request.user 
    data = request.data
    order_items = data.get('order_items') 

    if not order_items or len(order_items) == 0:
        return Response({'error': 'No order received'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        print(order_items)
        total_amount = sum(item['price'] * item['quantity'] for item in order_items)
        order = Order.objects.create(
            user = user,
            city = data['city'],
            street = data['street'],
            phone_no = data['phone_no'],
            country = data['country'],
            total_amount = total_amount,
        )
        for i in order_items:
            product = Product.objects.get(id=i['product'])
            item = OrderItem.objects.create(
                product= product,
                order = order,
                name = product.name,
                quantity = i['quantity'],
                price = i['price']
            )
            # product.stock -= item.quantity
            product.save()
        serializer = OrderSerializer(order,many=False)
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])
def update_order_status(request,pk):
    order = get_object_or_404(Order,id=pk)
    order.status = request.data['status']
    order.save()
    serializer = OrderSerializer(order,many=False)
    return  Response({"order":serializer.data})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_order(request,pk):
    order = get_object_or_404(Order,id=pk)

    order.delete()
    return  Response({"details":"deletion is done"})
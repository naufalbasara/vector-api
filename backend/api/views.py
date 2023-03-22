from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Product
from api.serializers import ProductSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    """
    Function to handle get, put, delete request for product data
    """
    try:
        product = Product.objects.get(pk=pk)
    except:
        return Response({"Status": status.HTTP_404_NOT_FOUND, "Message": "The data that have been requested not found."})
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        serializer = product.delete()
        return Response({"Status": status.HTTP_204_NO_CONTENT, "Message": "Product deleted."})


@api_view(['POST'])
def handling_data(request):
    if request.method == 'POST':
        product_serializer = ProductSerializer(data=request.data)
        if product_serializer.is_valid(raise_exception=True):
            product_serializer.save()
            return Response({"Status": status.HTTP_201_CREATED, "Message":f'Product have been created.'})
        return Response({"Status": status.HTTP_400_BAD_REQUEST, "Message":f'Bad data.'})
    
@api_view(['GET'])
def download_product_list(request):
    return
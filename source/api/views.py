from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api.serializers import ProductSerializer, OrderSerializer
from webapp.models import Product, Order


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')

class ProductViewSet(ViewSet):
    queryset = Product.objects.all()

    def list(self, request):
        objects = Product.objects.all()
        slr = ProductSerializer(objects, many=True, context={'request':request})
        return Response(slr.data)


    def create(self, request):
        slr = ProductSerializer(data=request.data, context={'request':request})
        if slr.is_valid():
            product = slr.save()
            return Response(slr.data)
        else:
            return Response(slr.errors, status=400)

    def update(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        slr = ProductSerializer(data=request.data, instance=product, context={'request':request})
        if slr.is_valid():
            product = slr.save()
            return Response(slr.data)
        else:
            return Response(slr.errors, status=400)

    def delete(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({'pk':pk})


class OrderViewSet(ViewSet):
    def list(self, request):
        objects = Order.objects.all()
        slr = OrderSerializer(objects, many=True, context={'request':request})
        return Response(slr.data)


    def create(self, request):
        slr = OrderSerializer(data=request.data, context={'request':request})
        if slr.is_valid():
            order= slr.save()
            return Response(slr.data)
        else:
            return Response(slr.errors, status=400)
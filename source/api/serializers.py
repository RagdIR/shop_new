from rest_framework import serializers
from webapp.models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='api:product-detail')

    class Meta:
        model = Product
        fields = [
            'name', 'description', 'category','amount', 'price',
        ]


class OrderSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='api:order-detail')
    product_display = ProductSerializer(many=True, read_only=True, source='products')

    class Meta:
        model = Order
        fields = [
            'name', 'phone', 'address', 'created_at', 'products',
        ]
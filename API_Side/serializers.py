from rest_framework import serializers
from API_Side.models import Store, Account, Product, Category, Customer, Order


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'mobile_num', 'first_name', 'date_joined']

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'store_name', 'address', 'store_link', 'owner']
        extra_kwargs = {
            'store_link': {'read_only': True},
        }


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.CharField()

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'MRP', 'sale_price', 'category', 'qty', 'store_name', 'image']
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['store_name'] = StoreSerializer(instance.store_name).data
        rep['category'] = CategorySerializer(instance.category).data
        return rep

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

    def display_value(self, instance):
        return instance.title



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'customer_email', 'customer_address']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'ordered_at', 'product', 'customer']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['store_name'] = ProductSerializer(instance.product).data
        rep['customer'] = CustomerSerializer(instance.customer).data
        return rep
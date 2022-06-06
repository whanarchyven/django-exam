from rest_framework.serializers import ModelSerializer
from .models import Partners, Client, Order


class PartnersSerializer(ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
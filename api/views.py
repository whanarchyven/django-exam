from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSerializer, ClientSerializer,PartnersSerializer
from .models import Order, Partners, Client
from rest_framework.generics import ListAPIView 
from rest_framework.decorators import action
from rest_framework.response import Response
import django_filters.rest_framework
from django.db.models import Q

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class GetOrderView(ListAPIView):
    queryset = Order.objects.filter(Q(price__gt=1500)|Q(client__name='Vova'))
    serializer_class = OrderSerializer


class PartnersViewSet(ModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class GetPartnersView(ListAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['organization', 'price']

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    @action(methods=['Delete'], detail=True, url_path='delete') 
    def delClient(self,request, pk=None):
        client=self.queryset.get(id=pk)
        client.delete()
        return Response('Пользователь был удален')
    @action(methods=['Post'], detail=False, url_path='post') 
    def posClient(self,request, pk=None):
        name=self.queryset.create(name=request.data.get('name'))
        name.save()
        return Response('Пользователь создан')
    


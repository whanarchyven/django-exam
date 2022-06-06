from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, ClientViewSet, GetOrderView,PartnersViewSet, GetPartnersView

router = DefaultRouter()
router.register('client', ClientViewSet )
router.register('partner', PartnersViewSet )
router.register('order', OrderViewSet )

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/order/filt', GetOrderView.as_view()),
    path('api/partner/filt', GetPartnersView.as_view()),
]

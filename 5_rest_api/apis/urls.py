from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()


urlpatterns = [
    path('v1/', include('apis.views.v1.urls'))
]

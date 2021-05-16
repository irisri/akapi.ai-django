from django.urls import path
from .views import property_upload, FilterPropertyList

app_name = 'property'
urlpatterns = [
    path('', property_upload, name="property_upload"),
    path('list/', FilterPropertyList.as_view(), name="property_filter"),
            ]
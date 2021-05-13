from django.urls import path
from .views import property_upload, PropertyList, FilterPropertyList

app_name = 'property'
urlpatterns = [
    path('', property_upload, name="property_upload"),
    path('list/', PropertyList.as_view(), name="property_list"),
    path('filter/', FilterPropertyList.as_view(), name="property_filter"),
            ]
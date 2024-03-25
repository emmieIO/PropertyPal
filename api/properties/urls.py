from django.urls import path
from .views import (
    all_properties,
    property_create,
    property_create_type,
    property_update,
    property_delete,
    property_update_type,
    property_type_delete,
)

app_name = "properties"

urlpatterns = [
    path("properties/", all_properties),
    path("properties/create-type", property_create_type),
    path("properties/upadte-type/<int:type_id>", property_update_type),
    path("properties/destroy/type/<int:type_id>", property_type_delete),
    path("properties/create", property_create),
    path("properties/update/<int:property_id>", property_update),
    path("properties/destroy/<int:property_id>", property_delete),
]

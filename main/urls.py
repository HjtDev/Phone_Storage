from django.urls import path
from .views import index, add_phone, phone_list, delete_phone, export_to_json, export_to_excel


app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('phones/', phone_list, name='phone_list'),
    path('phones/delete/<phone_id>/', delete_phone, name='delete_phone'),
    path('phones/export/json/', export_to_json, name='export_to_json'),
    path('phones/export/excel/', export_to_excel, name='export_to_excel'),
    path('phones/add/', add_phone, name='add_phone'),  # New URL for adding phones
]


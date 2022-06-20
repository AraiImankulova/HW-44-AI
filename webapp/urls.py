from django.urls import path

from webapp.views import calculate, calculate_operation

urlpatterns = [
    path('', calculate_operation),
    path('calculate', calculate_operation),
    path('calculate_operation', calculate_operation),

    ]
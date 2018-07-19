from django.urls import path
from api import views

urlpatterns = [
    path('api/', views.user_profile_data.as_view()	),
]
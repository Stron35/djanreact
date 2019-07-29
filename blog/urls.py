from django.urls import path
from .views import *

urlpatterns = [
	path('api/lead/', LeadListCreate.as_view() ),
]
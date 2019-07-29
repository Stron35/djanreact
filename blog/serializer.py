from rest_framework import serializers
from .models import *

class LeadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lead
		fields = ('id', 'name', 'message', 'email')
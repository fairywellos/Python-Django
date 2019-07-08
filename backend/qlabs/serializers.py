from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('strategy', 'date', 'quantity', 'entry', 'last_price', 'buy_or_sell', 'returns', 'equity')
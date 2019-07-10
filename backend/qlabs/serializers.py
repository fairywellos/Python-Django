from rest_framework import serializers
from .models import Log, MonthlyLog

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('strategy', 'date', 'current_date', 'quantity', 'entry', 'last_price', 'buy_or_sell', 'returns', 'equity')

class MonthlyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyLog
        fields = ('strategy', 'month', 'returns')
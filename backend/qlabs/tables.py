# tutorial/tables.py
import django_tables2 as tables
from .models import Log, MonthlyLog

class LogTable(tables.Table):

    class Meta:
        model = Log
        template_name = 'django_tables2/bootstrap.html'

class MonthlyLogTable(tables.Table):

    class Meta:
        model = MonthlyLog
        template_name = 'django_tables2/bootstrap.html'
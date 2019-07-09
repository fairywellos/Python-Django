from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView, View
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from src.main import get_today
import re

from .serializers import LogSerializer, MonthlyLogSerializer
from .models import Log, MonthlyLog

from .tables import LogTable, MonthlyLogTable
from django_tables2 import RequestConfig, MultiTableMixin
from django.views.generic.base import TemplateView


class LiveTableView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'live_today.html'

    def get(self, request, format=None):
        length = len(Log.objects.all())
        print (length)
        a = int(length) - 8
        b = int(length) - 5
        logs = Log.objects.all()[a:b]
        # last_ten = Messages.objects.all().order_by('-id')[:11]
        queryset = LogTable(logs)
        RequestConfig(request, paginate={'per_page': 10})

        serializer = LogSerializer(queryset, many=True)
        return Response({'serializer': serializer, 'logs': queryset})

class TestTableView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'test_today.html'

    def get(self, request, format=None):
        logs = Log.objects.exclude(strategy="LIVE_MA-1-21_LTC_USD").exclude(strategy="LIVE_MA-1-21_ETH_USD").exclude(strategy="LIVE_MA-1-21_BTC_USD")

        queryset = LogTable(logs)
        RequestConfig(request, paginate={'per_page': 10}).configure(queryset)

        serializer = LogSerializer(queryset, many=True)
        return Response({'serializer': serializer, 'logs': queryset})

class MonthlyTableView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'monthly.html'

    def get(self, request, format=None):
        logs = MonthlyLog.objects.all()

        queryset = MonthlyLogTable(logs)
        RequestConfig(request, paginate={'per_page': 10}).configure(queryset)

        serializer = MonthlyLogSerializer(queryset, many=True)
        return Response({'serializer': serializer, 'logs': queryset})

# class LogTablesView(MultiTableMixin, TemplateView):
#     print("I'm in LogTables")
#     template_name = "log_list.html"

#     logs_live = Log.objects.exclude(strategy="MA-1-21_BCH_USD").exclude(strategy="MA-1-21_BTC_USD").exclude(strategy="MA-1-21_BTC_USDT").exclude(strategy="MA-1-21_LTC_USD").exclude(strategy="MA-1-21_XMR_USD").exclude(strategy="MA-1-21_XRP_USD").exclude(strategy="MA-3x_XBTUSD").exclude(strategy="Test_BTC_EUR").order_by('-id')

#     logs_test = Log.objects.exclude(strategy="LIVE_MA-1-21_LTC_USD").exclude(strategy="LIVE_MA-1-21_ETH_USD").exclude(strategy="LIVE_MA-1-21_BTC_USD").order_by('-id')

#     table_pagination = {
#         'per_page': 10
#     }

#     tables = [
#         LogTable(logs_live, exclude=("id", )),
#         LogTable(logs_test, exclude=("id", ))
#     ]

class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        logs = Log.objects.order_by('date').values()
        filtered_logs = []
        for v in logs:
            if re.match('^LIVE', v['strategy']):
                filtered_logs.append(v)

        return Response(filtered_logs)

def index(request):
    result = get_today()
    list_values = [ v for v in result.values() ]
    print(list_values)
    serializer = LogSerializer(data=list_values, many=True)

    if serializer.is_valid():
        serializer.save()
        return HttpResponseRedirect(redirect_to="live")
    return HttpResponse("Failed")

# def getData(request):
#     logs = Log.objects.all()
#     serializer = LogSerializer(logs, many=True)
#     return Response(serializer.data)
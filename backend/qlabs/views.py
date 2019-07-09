from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView, View
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from src.main import get_today
import re

from .serializers import LogSerializer
from .models import Log

from .tables import LogTable
from django_tables2 import RequestConfig, MultiTableMixin
from django.views.generic.base import TemplateView


# class LogList(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'log_list.html'

#     def get(self, request, format=None):
#         logs = Log.objects.order_by('-id')

#         queryset = LogTable(logs)
#         RequestConfig(request, paginate={'per_page': 10}).configure(queryset)

#         serializer = LogSerializer(queryset, many=True)
#         return Response({'serializer': serializer, 'logs': queryset})

class LogTablesView(MultiTableMixin, TemplateView):
    template_name = "log_list.html"
    logs = Log.objects.order_by('-id')
    tables = [
        LogTable(logs, exclude=("id", )),
        LogTable(logs, exclude=("id", ))
    ]
    table_pagination = {
        'per_page': 10
    }

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
        return HttpResponse("Created Successfully!")
    return HttpResponse("Failed")

# def getData(request):
#     logs = Log.objects.all()
#     serializer = LogSerializer(logs, many=True)
#     return Response(serializer.data)
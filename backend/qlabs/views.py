from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from src.main import get_today

from .serializers import LogSerializer
from .models import Log

from .tables import LogTable
from django_tables2 import RequestConfig

class LogList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'log_list.html'

    def get(self, request, format=None):
        queryset = LogTable(Log.objects.all())
        RequestConfig(request).configure(queryset)
        print(queryset)
        serializer = LogSerializer(queryset, many=True)
        return Response({'serializer': serializer, 'logs': queryset})

# def index(request):
#     result = get_today()
#     list_values = [ v for v in result.values() ]
#     # print(list_values)
#     serializer = LogSerializer(data=list_values, many=True)

#     if serializer.is_valid():
#         serializer.save()
#         return HttpResponse("Created Successfully!")
#     return HttpResponse("Failed")

# def getData(request):
#     logs = Log.objects.all()
#     serializer = LogSerializer(logs, many=True)
#     return Response(serializer.data)
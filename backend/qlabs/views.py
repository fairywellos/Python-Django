from django.http import HttpResponse
from src.main import get_today
from .serializers import LogSerializer

def index(request):
    result = get_today()
    list_values = [ v for v in result.values() ]
    # print(list_values)
    serializer = LogSerializer(data=list_values, many=True)

    if serializer.is_valid():
        serializer.save()
        return HttpResponse("Created Successfully!")
    return HttpResponse("Failed")


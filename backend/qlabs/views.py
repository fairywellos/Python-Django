from django.http import HttpResponse
from src.main import get_today

def index(request):
    # print(get_today())
    result = get_today()
    print(result)
    return HttpResponse("Hello, world. You're at the polls index.")


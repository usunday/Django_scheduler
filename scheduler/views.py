from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
from scheduler.models import Member, ServingDay


# Create your views here.

def hello(request):
    """hello test page"""
    return render(request, 'hello.html')

def schedule(request):
    servertime = datetime.now()

    return render(request, 'schedule.html', {'servertime' : servertime.strftime("%Y-%m-%d %H:%M:%S")})

def monthlyList(request):
    """print all days with member"""
    # days = ServingDay.objects.all()
    days = ServingDay.objects.all().values('date', 'server__nickName', 'memo')
    days_list = list(days)
    #days_json = serializers.serialize('json', days, fields=('date', 'server'))

    return JsonResponse(days_list, safe=False)

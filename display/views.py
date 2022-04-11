from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import NoticeSerializer
from .models import Notice


# Create your views here.
def dept(request):
    return render (request,'dept.html')

def off(request): 
    return render(request,'off.html' )   


class NoticeViewset(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    
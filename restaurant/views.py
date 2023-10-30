from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializer import MenuSerializer, BookingSerializer
from .models import Menu


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = BookingSerializer

'''
Tips:

To declare the ViewSet class, you can use the following example:
'''
# class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all() 
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated] 
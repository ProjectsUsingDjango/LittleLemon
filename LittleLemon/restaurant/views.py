from django.shortcuts import render
from rest_framework import generics , viewsets
from .models import Menu , Booking
from .serializers import MenuSerializer , BookingSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import response


# token = Token.objects.create(user=.....)
#print(token.key)

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView , generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return response({"message":"This view is protected"})

# To secure view use following decorators above function or class
'''
    from rest_framework.decorators import api_view , permission_classes
    from rest_framework.permissions import IsAuthenticated

    @api_view()

    @permission_classes([IsAuthenticated])
'''
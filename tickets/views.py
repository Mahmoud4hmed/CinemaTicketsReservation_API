from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Guest, Movie, Reservation
from .serializers import GuestSerializer, ReservationSerializer, MovieSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.authentication import BaseAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def FBV_List(request):
    
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def FBV_pk(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CBV_List(APIView):
    def get(self, request):
        guest = Guest.objects.all()
        serializer = GuestSerializer(guest, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CBV_pk(APIView):
    def get_object_or_404(self, pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def find_movie(request):
    movies = Movie.objects.filter(
        movie=request.data['movie'],
        hall=request.data['hall'],
    )
    serializer = MovieSerializer(movies, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def new_reservation(request):
    movie = Movie.objects.get(
        hall = request.data['hall'],
        movie = request.data['movie'],
    )
    guest = Guest()
    guest.name = request.data['name']
    guest.phone = request.data['phone']
    guest.save()
    
    reservation = Reservation()
    reservation.guest = guest
    reservation.movie = movie
    reservation.save()
    
    serializer = ReservationSerializer(reservation)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def reservation_list(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)

class generics_list(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
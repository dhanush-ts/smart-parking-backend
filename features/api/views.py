from rest_framework.views import APIView
from features.api.Serializers import (CategorySerializer, UserSerializer, CategoryDataSerializer
                                      , NumberPlateSerializer, TransactionSerializer , ParkingSerializer)
from rest_framework.response import Response
from features.models import Category, User, NumberPlate, Tansaction, Parking, CategoryData
from rest_framework import status
from django.utils import timezone

class ParkingExitAV(APIView):
    def post(self, request):
        try:
            number_plate_value = request.data['number_plate']  # Get number_plate from the request
            exit_time = timezone.now()  # Get current time
            
            # Find the parking record for the number plate
            parking = Parking.objects.get(number_plate__number_plate=number_plate_value)
            
            # Ensure entry_time is timezone-aware
            if timezone.is_naive(parking.entry_time):
                entry_time = timezone.make_aware(parking.entry_time)
            else:
                entry_time = parking.entry_time
            
            # Calculate time spent
            time_spent = exit_time - entry_time
            
            # Get the cost per minute from the category data
            cost_per_minute = parking.category_data.cost_per_minute
            
            # Calculate total cost
            print(entry_time,exit_time,(time_spent.total_seconds() // 60) , cost_per_minute)
            total_cost = (time_spent.total_seconds() // 60) * cost_per_minute
            
            # Get the user associated with the number plate
            number_plate = NumberPlate.objects.get(number_plate=number_plate_value)
            user = number_plate.user  # Fetch the user from NumberPlate
            
            # Create a new transaction
            Tansaction.objects.create(
                user=user,
                category_data=parking.category_data,
                cost=total_cost
            )
            
            # Delete the parking entry
            parking.delete()
            
            return Response({"message": "Transaction completed", "total_cost": total_cost}, status=status.HTTP_200_OK)
        
        except Parking.DoesNotExist:
            return Response({"error": "Parking entry not found"}, status=status.HTTP_404_NOT_FOUND)
        except NumberPlate.DoesNotExist:
            return Response({"error": "Number plate not found"}, status=status.HTTP_404_NOT_FOUND)
 

class ParkingAV(APIView):
    def get(self, request):
        try:
            parking = Parking.objects.all()
            serializer = ParkingSerializer(parking, many=True)
            return Response(serializer.data)
        except Parking.DoesNotExist:
            return Response({'status':'not found'},status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        serializer = ParkingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionAV(APIView):
    def get(self, request):
        try:
            transactions = Tansaction.objects.all()
            serializer = TransactionSerializer(transactions, many=True)
            print(serializer.data)
            return Response(serializer.data)
        except Tansaction.DoesNotExist:
            return Response({'status':'not found'},status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NumberPlateAV(APIView):
    def get(self, request):
        try:
            number_plate = NumberPlate.objects.all()
            serializer = NumberPlateSerializer(number_plate, many=True)
            return Response(serializer.data)
        except NumberPlate.DoesNotExist:
            return Response({'status':'not found'},status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        serializer = NumberPlateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryListAV(APIView):
    def get(self, request):
        try:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)
    
        except Category.DoesnotExist:
            return Response({'status':'not found'},status=status.HTTP_404_NOT_FOUND)    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDataAV(APIView):
    def get(self, request):
        try:
            category_data = Category.objects.all()
            serializer = CategoryDataSerializer(category_data, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'status':'not found'},status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        serializer = CategoryDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDataDetails(APIView):
    def get(self, request, pk):
        try:
            category_data = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category_data)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'status':'not found'},status=status.HTTP_404_NOT_FOUND)
        
class TransactionUser(APIView):
    def get(self, request, pk):
        try:
            transactions = Tansaction.objects.filter(user=pk)
            serializer = TransactionSerializer(transactions, many=True)
            return Response(serializer.data)
        except Tansaction.DoesNotExist:
            return Response({'status':'not found'},status=status.HTTP_404_NOT_FOUND)

class Login(APIView):
    def post(self, request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            for i in serializer.data:
                if i['email'] == request.data['email']:
                    if i['password'] == request.data['password']:            
                        return Response(i)
                    return Response({"success": False, "message":"wrong password"})
                print(i['email'],request.data['email'])
            return Response({"success": False, "message":"user not found"})
        except User.DoesNotExist:
            return Response({'status':'not found'},status=status.HTTP_404_NOT_FOUND)
    
class UserListAV(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'status':'not found'},status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetailAV(APIView):
    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
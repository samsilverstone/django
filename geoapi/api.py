from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from knox.models import AuthToken


class DistrictView(APIView):

    permission_classes=[IsAuthenticated]

    def get(self,request):
        district=District.objects.all()
        serializer=DistrictSerializer(district,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
class DistrictDetailView(APIView):

    permission_classes=[IsAuthenticated]

    def get_object(self, pk):
        try:
            return District.objects.get(pk=pk)
        except District.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        district=self.get_object(pk)
        serializer=DistrictSerializer(district)
        return Response(serializer.data)

    def put(self,request,pk):
        district=self.get_object(pk)
        serializer=DistrictSerializer(instance=district,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        district=self.get_object(pk=pk)
        district.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
            

class RegistrationAPI(APIView):

    permission_classes=[AllowAny]

    def post(self,request):
        register=CreateUserSerializer(data=request.data)
        register.is_valid(raise_exception=True)
        user=register.save()
        return Response({
            # "user":user,
            "token":AuthToken.objects.create(user)[1]
        })

class LoginAPI(APIView):

    def post(self,request):
        login=LoginUserSerializer(data=request.data)
        login.is_valid(raise_exception=True)
        # user=login.validated_data
        return Response({
            # "user":user,
            "Token":AuthToken.objects.create(user)[1]
        })
            

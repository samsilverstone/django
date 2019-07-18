from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import exceptions
from .models import *


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email','password')
        extra_kwargs={'password':{'write_only':True}}

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            print("AUthenticating")
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                print("Inside block")
                if user.is_active:
                    print("returning")
                    return user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data


class DistrictSerializer(serializers.ModelSerializer):

    def create(self,validated_data):
        return District.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.district=validated_data.get('district',instance.district)
        instance.statename=validated_data.get('statename',instance.statename)
        instance.save()
        return instance
        
    class Meta:
        model=District
        fields='__all__'
    

class PincodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pincode
        fields='__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model=States
        fields='__all__'
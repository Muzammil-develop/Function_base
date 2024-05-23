from rest_framework import serializers
from ..models import Store

class StoreSerializer (serializers.ModelSerializer):
    class  Meta:
        model = Store
        fields = '__all__' 

def create (self , validated_data):
    return Store.objects,create (**validated_data)

def update (self , instance , validated_data):
    instance.name = validated_data.get ('name' , instance.name)
    instance.location = validated_data.get ('location' , instance.location)
    instance.active = validated_data.get ('active' , instance.active)
    instance.save ()
    return instance


from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'


class BlockSerializer(serializers.ModelSerializer):
    hall = HallSerializer()

    class Meta:
        model = Block
        fields = '__all__'


class RowSerializer(serializers.ModelSerializer):
    block = BlockSerializer()

    class Meta:
        model = Row
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    row = RowSerializer()

    class Meta:
        model = Seat
        fields = '__all__'

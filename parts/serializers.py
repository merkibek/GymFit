from rest_framework import serializers
from .models import Client, Attendance


class ClientSerializer(serializers.Serializer):
    class Meta:
        model = Client
        fields = (
            'client_id', 'first_name', 'last_name', 'phone', 'birth_date',)


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = 'client'

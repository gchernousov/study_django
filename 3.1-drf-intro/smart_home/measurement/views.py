from rest_framework import generics

from .models import Sensor, Measurement
from .serializers import SensorsSerializer, SensorDetailSerializer, NewMeasurementSerializer


class SensorsView(generics.ListCreateAPIView):
    """GET и POST запросы для датчиков"""
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class SensorDetailView(generics.RetrieveUpdateAPIView):
    """GET, PUT и PATCH запросы для конкретного датчика"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(generics.CreateAPIView):
    """POST запрос для измерений"""
    queryset = Measurement.objects.all()
    serializer_class = NewMeasurementSerializer
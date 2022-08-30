from django.urls import path
from .views import SensorsView, SensorDetailView, MeasurementView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<int:pk>/', SensorDetailView.as_view()),
    path('measurement/', MeasurementView.as_view())
]

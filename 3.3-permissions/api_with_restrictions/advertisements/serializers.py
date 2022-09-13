from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        # Проверяю, есть ли в запросе ключ [status]
        # Если да, пусть status равен значению ключа [status] (либо OPEN, либо CLOSED)
        # Если нет, пусть все равно равен OPEN (т.к. это значение идет по умолчанию)
        # Условие: если у текущего пользователя кол-во открытых объявлений 10 и status = OPEN
        # (т.е. либо идет POST запрос со статусом по умолчанию, либо PATCH со сменой статуса с CLOSED на OPEN)
        # то выходит ошибка и data не возвращается для дальнейшей обработки
        status = data["status"] if 'status' in data else "OPEN"
        current_user = self.context["request"].user
        open_adverts = Advertisement.objects.filter(creator=current_user.id, status='OPEN')
        if len(open_adverts) >= 10 and status == 'OPEN':
            raise ValidationError({'Ошибка!': 'У вас не может быть больше 10 открытых объявлений!'})
        return data

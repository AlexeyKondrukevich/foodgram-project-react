from rest_framework import serializers
from recipes.models import Tag
from django.contrib.auth import authenticate


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            "id",
            "name",
            "color",
            "slug",
        )


from rest_framework import serializers


class ObtainTokenSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=254, required=True)
    password = serializers.CharField(required=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        fields = ("password", "email")

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        if email and password:
            user = authenticate(
                request=self.context.get("request"),
                email=email,
                password=password,
            )
            if not user:
                raise serializers.ValidationError(
                    "Проверте электронную почту и пароль"
                )
        else:
            raise serializers.ValidationError(
                "Введите электронную почту и пароль"
            )
        attrs["user"] = user
        return attrs

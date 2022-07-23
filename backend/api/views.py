from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import ObtainTokenSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .serializers import TagSerializer
from recipes.models import Tag


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ObtainToken(APIView):
    # permission_classes = (AllowAny,)

    # def post(self, request):
    #     serializer = ObtainTokenSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     token = RefreshToken.for_user(request.user).access_token
    #     return Response(
    #         {"auth_token": str(token)},
    #         status=status.HTTP_201_CREATED,
    #     )
    serializer_class = ObtainTokenSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = ObtainTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {"auth_token": token.key}, status=status.HTTP_201_CREATED
        )

from rest_framework import mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from movies_rest_app.auth.serializers import UserSerializer, SignupSerializer


class IsStaffPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsStaffPermission])
def me(request):
    s = UserSerializer(instance=request.user)
    return Response(data=s.data)


@api_view(['POST'])
def signup(request):
    s = SignupSerializer(data=request.data)
    s.is_valid(raise_exception=True)
    s.save()
    return Response(data=s.data)

# class SignupView(mixins.CreateModelMixin,
#                    GenericViewSet):
#     queryset = User.objects.all()
#     serializer_class = SignupSerializer
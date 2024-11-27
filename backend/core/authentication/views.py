from rest_framework import views, viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from core.authentication.serializers import UserWriteSerializer, UserReadSerializer, MeSerializer, \
    ChangePasswordSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by('-id')
    write_serializer = UserWriteSerializer
    read_serializer = UserReadSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return self.read_serializer
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return self.write_serializer
        return self.serializer_class

    @action(detail=False, serializer_class=MeSerializer)
    def me(self, request):
        self.kwargs['pk'] = request.user.pk
        return super().retrieve(request)

    @action(detail=True, methods=['put'], url_path='change-password', serializer_class=ChangePasswordSerializer)
    def change_password(self, request, pk=None):
        super().update(request)
        return Response({'detail': 'Password changed'})
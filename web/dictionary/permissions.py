from rest_framework.permissions import BasePermission
from django.conf import settings


class HasAPISecret(BasePermission):
    key = settings.API_SECRET

    def has_permission(self, request, view):
        request_secret = request.headers.get('Api-Secret')

        return request_secret == self.key

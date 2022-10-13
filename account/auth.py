from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from .models import School, Student
from .token import decode_access_token


class JWTAuth(BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META["HTTP_AUTHORIZATION"]
            prefix, token = token.split()
            if prefix != "Bearer":
                raise exceptions.AuthenticationFailed
            payload = decode_access_token(token)
            obj = School.objects.filter(id=payload["id"]) or Student.objects.filter(
                id=payload["id"]
            )
            if not obj:
                raise exceptions.AuthenticationFailed

            return obj.first(), payload
        except (KeyError, ValueError):
            raise exceptions.AuthenticationFailed
        except Exception as e:
            raise exceptions.AuthenticationFailed(str(e))

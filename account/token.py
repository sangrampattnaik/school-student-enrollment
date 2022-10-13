import datetime

import jwt
from django.conf import settings
from rest_framework import exceptions


def get_access_token(id: int, user_type: str):
    return jwt.encode(
        {
            "id": id,
            "user_type": user_type,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
        },
        settings.SECRET_KEY,
    )


def decode_access_token(token):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except:
        raise exceptions.AuthenticationFailed(detail="unauthorized request")

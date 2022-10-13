import re

from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework import exceptions, generics, response

from account.auth import JWTAuth

from .models import School, Student
from .permissions import IsSchoolUser
from .serializers import LoginSerializer, SchoolSerializer, StudentSerializer
from .token import get_access_token


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        self.serializer_class(data=request.data).is_valid(raise_exception=True)
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.fullmatch(regex, request.data["username_or_email"]):
            obj = User.objects.filter(username=request.data["username_or_email"])
            if obj.exists():
                raise exceptions.AuthenticationFailed(
                    detail="admin login not implemnted... it will be updated in next version"
                )
            obj = Student.objects.filter(username=request.data["username_or_email"])
            if not obj.exists():
                raise exceptions.AuthenticationFailed
            else:
                user_type = "student"
        else:
            obj = School.objects.filter(email=request.data["username_or_email"])
            if not obj.exists():
                raise exceptions.AuthenticationFailed
            user_type = "school"
        obj = obj.first()
        if not check_password(request.data["password"], obj.password):
            raise exceptions.AuthenticationFailed
        data = {"token": get_access_token(id=obj.id, user_type=user_type)}
        return response.Response(data)


class SchoolCreateAPIView(generics.CreateAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()


class StudentCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    authentication_classes = [JWTAuth]
    permission_classes = [IsSchoolUser]

    def get(self, request, *args, **kwargs):
        grade = request.GET.get("grade")
        queryset = self.queryset.filter(school_id=request.user.id)
        if grade:
            queryset = self.queryset.filter(grade=grade)
        data = self.serializer_class(queryset, many=True).data
        return response.Response(data)

    def post(self, request):
        if isinstance(request.data, list):
            serializer = self.serializer_class(data=request.data, many=True)
        else:
            serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()
        return response.Response(serializer.data, status=201)

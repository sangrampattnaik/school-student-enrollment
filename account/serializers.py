from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import School, Student


class LoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField()
    password = serializers.CharField()


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"

    def create(self, validated_data):
        validated_data["password"] = make_password(
            validated_data["password"]
        )  # password hasnhing
        return super().create(validated_data)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate(self, attrs):
        grade = attrs.get("grade", 0)
        if grade not in range(1, 13):
            raise serializers.ValidationError("grade invalid... should be 1 to 12")
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data["password"] = make_password(
            validated_data["password"]
        )  # password hasnhing
        return super().create(validated_data)

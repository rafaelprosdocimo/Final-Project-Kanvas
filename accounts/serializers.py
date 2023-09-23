from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Account
        fields = ["id", "username", "email", "password", "is_superuser"]
        extra_kwargs = {
            "password": {"write_only": True},
        }
    
    def create(self, validated_data: dict) -> Account:

        if validated_data.get("is_superuser"):
            return Account.objects.create_superuser(**validated_data)
        else:
            return Account.objects.create_user(**validated_data)

from rest_framework import serializers
from . models import User


class UserRegisterSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(write_only=True, required=True)

	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'password', 'password2')
		extra_kwargs = {
			'password': {'write_only':True},
		}

	def create(self, validated_data):
		del validated_data['password2']
		return User.objects.create_user(**validated_data)


	def validate(self, data):
		if data['password'] != data['password2']:
			raise serializers.ValidationError('passwords must match')
		return data


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']
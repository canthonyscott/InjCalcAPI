from rest_framework import serializers
from oligos.models import Oligo
from django.contrib.auth.models import User

class OligoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Oligo
        fields = ('pk', 'gene', 'molecular_weight', 'owner', 'added_by')



class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'pk','password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User()
        user.set_password(validated_data['password'])
        validated_data['password'] = user.password
        return super(UserSerializer, self).create(validated_data)
from rest_framework import serializers
from recommender.models import User, Movie


# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     created = serializers.DateTimeField(read_only=True)
#     mov_id = serializers.IntegerField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'created', 'mov_id']


    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.time_create = validated_data.get('time_create', instance.time_create)
        instance.mov_id = validated_data.get('mov_id', instance.mov_is)
        instance.save()
        return instance
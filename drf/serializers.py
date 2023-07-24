from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')
    created_at = serializers.SerializerMethodField()


updated_at = serializers.SerializerMethodField()


def get_created_at(self, obj):
    return naturaltime(obj.created_at)


def get_updated_at(self, obj):
    return naturaltime(obj.updated_at)


class Meta(UserDetailsSerializer.Meta):
    fields = UserDetailsSerializer.Meta.fields + \
        ('profile_id', 'profile_image')

from rest_framework import serializers
from hamayesh.models import Hamayesh, ParticipantHamayesh
from django_jalali.serializers.serializerfield import JDateField, JDateTimeField
from jalali_date.fields import JalaliDateField
from django.contrib.auth import get_user_model


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = [
            'email', 'mobile', 'first_name', 'last_name'
        ]


class ParticipantsSerializer(serializers.ModelSerializer):
    hamayesh = serializers.StringRelatedField()

    class Meta:
        model = ParticipantHamayesh
        fields = ['hamayesh', 'full_name', 'email', 'mobile_number', 'hamayesh']


class HamayeshSerializer(serializers.ModelSerializer):
    participant_count = serializers.SerializerMethodField()
    # date_of_hamayesh = JDateTimeField()
    # hamayesh_detail_url = serializers.HyperlinkedIdentityField(view_name='hamayesh:api-v1:hamayesh-detail')

    class Meta:
        model = Hamayesh
        fields = ['id', 'title', 'description', 'owner', 'image',
         'participant_count', 'date_of_hamayesh', 'location', 'status']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['participants'] = ParticipantsSerializer(instance.participants.all(), many=True).data
        rep['owner'] = OwnerSerializer(instance.owner).data
        return rep

    def get_participant_count(self, hamayesh):
        h = hamayesh.participants.all().count()
        return h
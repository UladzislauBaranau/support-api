from api.v1.profiles.serializers import ProfileSerializer, UpdateSupportStatusSerializer

from django.forms.models import model_to_dict


def test_profile_serializer(test_user):
    serialized_data = model_to_dict(test_user)
    serializer = ProfileSerializer(data=serialized_data)

    assert serializer.is_valid()
    assert serializer.errors == {}


def test_update_support_status_serializer(test_user):
    serialized_data = model_to_dict(test_user)
    serializer = UpdateSupportStatusSerializer(data=serialized_data)

    # only 'user' and 'is_support' fields are used for serialization
    assert len(serializer.fields) == 2

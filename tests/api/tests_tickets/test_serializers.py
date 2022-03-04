import pytest

from api.v1.tickets.serializers import TicketsInfoSerializer

from tickets.models import Ticket


@pytest.fixture
def test_serialize_model(db):
    t = Ticket.objects.create()
    expected_serialized_data = {
        'ticket_id': t.ticket_id,
        'ticket_author': 'testuser',
        'content': t.content,
        'ticket_status': t.ticket_status,
    }
    serializer = TicketsInfoSerializer(t)

    assert serializer.data == expected_serialized_data
    assert serializer.is_valid(raise_exception=True)
    assert serializer.errors == {}

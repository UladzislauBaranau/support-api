import pytest

from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from tickets.models import Message, Ticket

User = get_user_model()


@pytest.fixture
def test_user(db):
    user = User.objects.create_user(
        username='testuser',
        email='testemail@test.com',
    )
    return user


@pytest.fixture
def api_client_user(test_user):
    client = APIClient()
    client.force_authenticate(test_user)
    return client


@pytest.fixture
def test_support(db):
    user = User.objects.create_user(
        username='support',
        email='support@test.com',
    )
    user.profile.is_support = True
    return user


@pytest.fixture
def api_client_support(test_support):
    client = APIClient()
    client.force_authenticate(test_support)
    return client


@pytest.fixture
def test_superuser(db):
    user = User.objects.create_superuser(
        username='admin',
        email='admin@test.com',
    )
    return user


@pytest.fixture
def api_client_superuser(test_superuser):
    client = APIClient()
    client.force_authenticate(test_superuser)
    return client


@pytest.fixture
def test_ticket(db, test_user):
    ticket = Ticket.objects.get_or_create(
        ticket_id='9ie346',
        ticket_author=test_user.profile,
        content='Test ticket',
    )
    return ticket


@pytest.fixture
def test_message(db, test_ticket, test_support):
    message = Message.objects.get_or_create(
        ticket=Ticket.objects.get(ticket_id='9ie346'),
        message_author=test_support.profile,
        message='Message from support',
    )
    return message

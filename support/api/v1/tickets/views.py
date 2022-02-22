from django.core.exceptions import ValidationError

from profiles.models import Profile
from tickets.models import Message, Ticket

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .permissions import IsSupportOrReadOnly, IsUserNotSupport
from .serializers import MessageSerializer, TicketSerializer, TicketsInfoSerializer, UpdateTicketStatusSerializer
from ..tasks import send_new_message_email, send_ticket_created_email


class CreateTicketView(generics.CreateAPIView):
    """Tickets can be created by all users except support.
    The user is sent an email confirming the creation of the ticket.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, IsUserNotSupport]

    def perform_create(self, serializer):
        content = self.request.data['content'].strip()
        queryset = Ticket.objects.filter(content=content)
        if queryset.exists():
            raise ValidationError('You have already create this ticket')

        ticket_author = Profile.objects.get(user=self.request.user)
        serializer.save(ticket_author=ticket_author)

        send_ticket_created_email.delay(self.request.user.email)


class ListTicketsView(generics.ListAPIView):
    """Users can view the tickets list."""
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]


class UpdateTicketStatusView(generics.RetrieveUpdateAPIView):
    """Ticket status update is only available to support."""
    queryset = Ticket.objects.all()
    serializer_class = UpdateTicketStatusSerializer
    permission_classes = [IsAuthenticated, IsSupportOrReadOnly]
    lookup_field = 'ticket_id'


class CreateMessageView(generics.ListCreateAPIView):
    """Each user can leave comments on tickets.
    The author of the ticket receives an email with the response.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        ticket_id = self.kwargs.get('ticket_id')
        ticket = Ticket.objects.get(ticket_id=ticket_id)
        message_author = Profile.objects.get(user=self.request.user)
        serializer.save(ticket=ticket, message_author=message_author)

        send_new_message_email.delay(ticket.ticket_author.user.email)


class UserTicketsListView(generics.ListAPIView):
    """User can view a list of his tickets."""
    serializer_class = TicketsInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        ticket_author = Profile.objects.get(user=self.request.user)
        return Ticket.objects.filter(ticket_author=ticket_author)

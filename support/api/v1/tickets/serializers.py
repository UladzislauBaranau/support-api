from rest_framework import serializers

from tickets.models import Message, Ticket


class TicketSerializer(serializers.ModelSerializer):
    ticket_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class UpdateTicketStatusSerializer(serializers.ModelSerializer):
    ticket_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Ticket
        read_only_fields = ['content']
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    ticket = serializers.StringRelatedField(read_only=True)
    message_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Message
        fields = '__all__'


class TicketsInfoSerializer(serializers.ModelSerializer):
    message = serializers.StringRelatedField(many=True)

    class Meta:
        model = Ticket
        fields = ['content', 'ticket_status', 'message']

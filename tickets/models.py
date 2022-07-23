import uuid

from django.db import models

from profiles.models import Profile


def generate_ticket_id():
    return str(uuid.uuid4())[:6]


class TimestampModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Ticket(TimestampModel):

    class Status(models.TextChoices):
        RESOLVED = 'RS', 'Resolved'
        UNRESOLVED = 'UN', 'Unresolved'
        DEFERRED = 'DF', 'Deferred'

    ticket_id = models.CharField(max_length=6, blank=True, unique=True, primary_key=True)
    ticket_author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    ticket_status = models.CharField(max_length=2, choices=Status.choices, default=Status.UNRESOLVED)

    def save(self, *args, **kwargs):
        if len(self.ticket_id) == 0:
            self.ticket_id = generate_ticket_id()
        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return f'author: {self.ticket_author}, ' \
               f'id: {self.ticket_id}, ' \
               f'status: {self.ticket_status}'

    class Meta:
        ordering = ('date_created', )


class Message(TimestampModel):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='message')
    message_author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)

    def __str__(self):
        return f'author: {self.message_author}, ' \
               f'message: {self.message[:50]}'

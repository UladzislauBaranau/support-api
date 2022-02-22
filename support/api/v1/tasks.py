from django.core.mail import send_mail

from support.celery import app

from tickets.models import Message


@app.task
def send_ticket_created_email(user_email):
    send_mail(
        'Your ticket has been successfully created',
        'Thank you for contacting us.\n'
        '\n'
        'We are already working on your question.',
        'support_app@gmail.com',
        [user_email],
        fail_silently=False,
    )


@app.task
def send_new_message_email(user_email):
    last_message = Message.objects.last()

    send_mail(
        'Your have a new message',
        f'Author: {last_message.message_author}.\n'
        '\n'
        f'Message: {last_message.message}.',
        'support_app@gmail.com',
        [user_email],
        fail_silently=False,
    )

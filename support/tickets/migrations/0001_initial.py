import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('ticket_id', models.CharField(
                    blank=True,
                    max_length=6,
                    primary_key=True,
                    serialize=False,
                    unique=True,
                ),
                 ),
                ('content', models.TextField(max_length=200)),
                ('ticket_status', models.CharField(
                    choices=[('RESOLVED', 'Resolved'),
                             ('UNRESOLVED', 'Unresolved'),
                             ('DEFERRED', 'Deferred')],
                    default='UNRESOLVED',
                    max_length=10),
                 ),
                ('ticket_author', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='profiles.profile',
                ),
                 ),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('message', models.TextField(max_length=500)),
                ('message_author', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='profiles.profile',
                ),
                 ),
                ('ticket', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='message',
                    to='tickets.ticket',
                ),
                 ),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

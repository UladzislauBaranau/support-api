from django.urls import path

from .views import CreateMessageView, CreateTicketView, ListTicketsView, UpdateTicketStatusView, UserTicketsListView

urlpatterns = [
    path('create-ticket/', CreateTicketView.as_view()),
    path('all/', ListTicketsView.as_view()),
    path('my-tickets/', UserTicketsListView.as_view()),
    path('<ticket_id>/message/', CreateMessageView.as_view()),
    path('<ticket_id>/', UpdateTicketStatusView.as_view()),
]

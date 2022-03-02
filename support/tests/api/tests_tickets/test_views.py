from rest_framework import status


def test_create_ticket_success(api_client_user):
    endpoint = '/api/v1/tickets/create-ticket/'
    request_data = {
        'content': 'Testing ticket from test_user',
    }
    response = api_client_user.post(endpoint, data=request_data)
    assert response.status_code == status.HTTP_201_CREATED


def test_create_ticket_fail_author_is_support(api_client_support):
    endpoint = '/api/v1/tickets/create-ticket/'
    request_data = {
        'content': 'Testing ticket from support',
    }
    response = api_client_support.post(endpoint, data=request_data)
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_create_ticket_fail_missing_content(api_client_user):
    endpoint = '/api/v1/tickets/create-ticket/'
    request_data = {}
    response = api_client_user.post(endpoint, data=request_data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_get_list_tickets(api_client_user, test_ticket):
    endpoint = '/api/v1/tickets/all/'
    response = api_client_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK

    data = response.data
    assert isinstance(data, list)
    assert len(data) == 1


def test_update_ticket_status_success(api_client_support, test_ticket):
    ticket_id = test_ticket[0].ticket_id
    endpoint = f'/api/v1/tickets/{ticket_id}/'
    request_data = {
        'ticket_status': 'RS',
    }
    response = api_client_support.put(endpoint, data=request_data)
    assert response.status_code == status.HTTP_200_OK


def test_update_ticket_status_fail(api_client_user, test_ticket):
    ticket_id = test_ticket[0].ticket_id
    endpoint = f'/api/v1/tickets/{ticket_id}/'
    request_data = {
        'ticket_status': 'DF',
    }
    response = api_client_user.put(endpoint, data=request_data)
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_get_user_tickets_list(api_client_user, test_ticket):
    endpoint = '/api/v1/tickets/my-tickets/'
    response = api_client_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK


def test_messages_list(api_client_user, test_ticket, test_message):
    ticket_id = test_ticket[0].ticket_id
    endpoint = f'/api/v1/tickets/{ticket_id}/message/'
    response = api_client_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK

    data = response.data
    assert len(data) == 1


def test_create_message(api_client_user, test_ticket, test_message):
    ticket_id = test_ticket[0].ticket_id
    endpoint = f'/api/v1/tickets/{ticket_id}/message/'
    request_data = {
        'message': 'New message',
    }
    post_response = api_client_user.post(endpoint, data=request_data)
    assert post_response.status_code == status.HTTP_201_CREATED

    get_response = api_client_user.get(endpoint)
    data = get_response.data
    assert get_response.status_code == status.HTTP_200_OK
    assert isinstance(data, list)
    assert len(data) == 2

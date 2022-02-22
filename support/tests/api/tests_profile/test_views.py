from rest_framework import status


def test_get_list_profile(api_client_user, test_superuser, test_user):
    endpoint = '/api/v1/profiles/all/'
    response = api_client_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK

    data = response.data
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["id"] == test_user.id
    assert data[1]["id"] == test_superuser.id


def test_put_support_status_success(api_client_superuser, test_user):
    pk = test_user.id
    endpoint = f'/api/v1/profiles/update-support/{pk}/'
    request_data = {
        'is_support': True,
    }
    response = api_client_superuser.put(endpoint, data=request_data)
    assert response.status_code == status.HTTP_200_OK

    response_data = response.data
    for key, value in request_data.items():
        assert response_data[key] == value


def test_put_support_status_fail(api_client_user, test_user):
    pk = test_user.id
    endpoint = f'/api/v1/profiles/update-support/{pk}/'
    request_data = {
        'is_support': True,
    }
    response = api_client_user.put(endpoint, data=request_data)
    assert response.status_code == status.HTTP_403_FORBIDDEN

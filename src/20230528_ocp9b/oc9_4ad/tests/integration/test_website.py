from django.urls import reverse


def test_mysite_is_online(client):
    """ test if the site is online """
    response = client.get(reverse("fadapp:home"))
    assert response.status_code == 200

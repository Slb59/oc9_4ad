from django.urls import resolve
from fad.fadapp.views import home


def test_verify_root_url_maps_to_home():
    match = resolve('/')
    assert match.func == home
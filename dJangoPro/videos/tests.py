import pytest
from django.urls import reverse


@pytest.fixture
def resp(client):
    return client.get(reverse('videos:video', args=('demonstracao',)))

def test_status_code(resp):
    assert resp.status_code==200
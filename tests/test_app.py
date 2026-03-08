import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, programs

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_get(client):
    """Test GET request to home page"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'ACEest FUNCTIONAL FITNESS' in response.data
    assert b'Client Profile' in response.data

def test_home_post_fat_loss(client):
    """Test POST request with Fat Loss program selection"""
    response = client.post('/', data={'program': 'Fat Loss (FL)'})
    assert response.status_code == 200
    assert b'ACEest FUNCTIONAL FITNESS' in response.data
    assert b'Back Squat' in response.data

def test_home_post_muscle_gain(client):
    """Test POST request with Muscle Gain program selection"""
    response = client.post('/', data={'program': 'Muscle Gain (MG)'})
    assert response.status_code == 200
    assert b'Squat 5x5' in response.data

def test_home_post_beginner(client):
    """Test POST request with Beginner program selection"""
    response = client.post('/', data={'program': 'Beginner (BG)'})
    assert response.status_code == 200
    assert b'Circuit Training' in response.data

def test_static_css_loaded(client):
    """Test that static CSS file is served correctly"""
    response = client.get('/static/style.css')
    assert response.status_code == 200
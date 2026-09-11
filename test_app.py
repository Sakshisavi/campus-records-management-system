import pytest
from app import app 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test if the home route loads successfully by following Redirects"""
    response = client.get('/',follow_redirects=True)
    assert response.status_code == 200

def test_invalid_route(client):
    """Test 404 response for non-existent routes."""
    response = client.get('/non-existent-page')
    assert response.status_code == 404

def test_login_page_loads(client):
    """Verify the login page renders properly"""
    response = client.get('/login')
    assert response.status_code ==200

def test_unauthorized_access(client):
    """Verify protected routes redirect non-logged-in users"""
    response = client.get('/index', follow_redirects=False)
    assert response.status_code in [302,401]

def test_login_submission(client):
    """Test submitting login credentials."""
    response = client.post('/login', data={
        'Admin_id`': '9',
        'password': '12'
    }, follow_redirects=True)
    # Checks that the app responds correctly (e.g., re-renders page or shows flash message)
    assert response.status_code in [200 ,400]   

    


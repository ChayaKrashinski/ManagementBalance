import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user():
    # מידע למשתמש חדש
    new_user_data = {
        "id": 1,  # ניתן לשנות ערכים כדי להתאים לנסיון הרצוי
        "name": "test_user",
        "password": "password123",
        "mail": "test@example.com"
    }
    # קריאה לנתיב הרלוונטי עם POST ושליחת המידע
    response = client.post("/user/register", json=new_user_data)
    assert response.status_code == 200
    assert response.json() == new_user_data

def test_login_user():
    # מידע לכניסת משתמש
    user_data = {
        "id":1,
        "name": "test_user",
        "password": "password123",
        "mail": "test@example.com"
    }
    # קריאה לנתיב הרלוונטי עם GET ושליחת המידע
    response = client.get("/user/login", json=user_data)
    assert response.status_code == 200
    assert response.json() == user_data

def test_update_user():
    # נתוני העדכון
    updated_user_data = {
        "name": "updated_user",
        "password": "updated_password",
        "mail": "updated@example.com"
    }
    # קריאה לנתיב הרלוונטי עם PUT ושליחת מזהה המשתמש והמידע לעדכון
    response = client.put("/user/", params={"id": 1}, json=updated_user_data)
    assert response.status_code == 200
    assert response.json() == {"message": "User updated successfully"}

def test_get_all_users():
    # קריאה לנתיב הרלוונטי עם GET
    response = client.get("/user/get_all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

from fastapi import APIRouter
from src.services.auth_service import login_user, register_user

router = APIRouter()

@router.get("/tasks")
def get_tasks():
    return {"tasks": ["Task 1", "Task 2"]}

@router.post("/register")
def register(username: str, password: str):
    return register_user(username, password)

@router.post("/login")
def login(username: str, password: str):
    return login_user(username, password)
from fastapi import APIRouter, Depends, FastAPI

from src.auth.auth import auth_backend, current_active_user, fastapi_users
from src.user.model import User
from src.user.schemas import SUserCreate, SUserRead, SUserUpdate


def add_auth_routes(app: FastAPI):
    app.include_router(
        fastapi_users.get_auth_router(auth_backend), prefix="/auth", tags=["auth"]
    )
    app.include_router(
        fastapi_users.get_register_router(SUserRead, SUserCreate),
        prefix="/auth",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users.get_reset_password_router(),
        prefix="/auth",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users.get_verify_router(SUserRead),
        prefix="/auth",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users.get_users_router(SUserRead, SUserUpdate),
        prefix="/users",
        tags=["users"],
    )

    @app.get("/authenticated-route")
    async def authenticated_route(user: User = Depends(current_active_user)):
        return {"message": f"Hello {user.email}!"}

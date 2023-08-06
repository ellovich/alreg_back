from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin

from src.admin.views import DoctorAdmin, PatientAdmin, RoleAdmin, UsersAdmin
from src.auth.auth import add_auth_routes
from src.database import engine

app = FastAPI(
    title="Регистр Алмазова",
    version="0.1.0",
#    root_path="/api"
)

@app.get("/")
def hello():
    return "Hello"

add_auth_routes(app)

# Подключение CORS, чтобы запросы к API могли приходить из браузера 
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5713", # React.js 
    ],
    allow_credentials=True,
    allow_methods=[
        "GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"
    ],
    allow_headers=[
        "Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", 
        "Access-Control-Allow-Origin",
        "Authorization"
    ],
)

# Подключение админки
admin = Admin(app, engine, title="Регистр Алмазова")
#admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.add_view(RoleAdmin)
admin.add_view(UsersAdmin)
admin.add_view(DoctorAdmin)
admin.add_view(PatientAdmin)
# admin.add_view(DoctorPatientAdmin)
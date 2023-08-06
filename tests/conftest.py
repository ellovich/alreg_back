import asyncio
import json
from datetime import datetime, date
from sqlalchemy import bindparam

import pytest
from httpx import AsyncClient
from sqlalchemy import insert

from src.config import settings
from src.database import BaseAlchemyModel, async_session_maker, engine
from src.doctor.model import Doctor
from src.main import app as fastapi_app
from src.patient.model import Patient, doctor_patient
from src.user.model import Role, User



@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    # Обязательно убеждаемся, что работаем с тестовой БД
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        # Удаление всех заданных нами таблиц из БД
        await conn.run_sync(BaseAlchemyModel.metadata.drop_all)
        # Добавление всех заданных нами таблиц из БД
        await conn.run_sync(BaseAlchemyModel.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"tests/mock_files/mock_{model}.json", encoding="utf-8") as file:
            return json.load(file)

    users = open_mock_json("users")
    roles = open_mock_json("roles")
    doctors = open_mock_json("doctors")
    patients = open_mock_json("patients")
    doctors_patients = open_mock_json("doctors_patients")
    # chats = open_mock_json("chats")

    # SQLAlchemy не принимает дату в текстовом формате, поэтому форматируем к datetime
    def fix_date(date):
        if date:
            if(len(date) > 8):
                return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
            else:
                return datetime.strptime(date, "%Y-%m-%d")

    for rows in [users, roles, doctors, patients]:
        for row in rows:
            row["created_on"] = fix_date(row["created_on"])
            row["updated_on"] = fix_date(row["updated_on"])
    for rows in [doctors, patients]:
        for row in rows:
            row["birth"] = datetime.strptime(row["birth"], "%Y-%m-%d")

    async with async_session_maker() as session:
        for Model, values in [
            (Doctor, doctors),
            (Patient, patients),
            (doctor_patient, doctors_patients),
            (Role, roles),
            (User, users),
        ]:   
            query = insert(Model).values(values)
            await session.execute(query)

        await session.commit()


# Взято из документации к pytest-asyncio
# Создаем новый event loop для прогона тестов
@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def ac():
    "Асинхронный клиент для тестирования эндпоинтов"
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="session")
async def authenticated_ac():
    "Асинхронный аутентифицированный клиент для тестирования эндпоинтов"
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        await ac.post(
            "/api/auth/login",
            json={
                "email": "ivan@test.com",
                "password": "string",
            },
        )
        assert ac.cookies["fastapiusersauth"]
        yield ac

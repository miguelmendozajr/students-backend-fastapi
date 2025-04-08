import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.handlers.students import StudentHttpHandler
from app.api.controllers.students import StudentController

class TestStudentHttpHandler:
    @pytest.fixture
    def mock_controller(self):
        controller = MagicMock()
        controller.get_all = AsyncMock()
        return controller
    
    @pytest.fixture
    def test_app(self, mock_controller):
        app = FastAPI()
        
        handler = StudentHttpHandler(mock_controller)
        
        @app.get("/students")
        async def get_students():
            return await handler.get_all_students()
        
        return app
    
    @pytest.fixture
    def test_client(self, test_app):
        return TestClient(test_app)
    
    def test_get_all_students(self, test_client, mock_controller):
        students = [
            {'matricula': 'A01234354', 'nombre': 'Miguel Mendoza', 'estatus': "Reestructura"},
            {'matricula': 'A01234355', 'nombre': 'Fernando Monroy', 'estatus': "Aprobado"},
            {'matricula': 'A01234356', 'nombre': 'Regina Cavazos', 'estatus': "Expulsado"},
            {'matricula': 'A01234357', 'nombre': 'Jorge Salcedo', 'estatus': "Pendiente"}
        ]
        
        mock_controller.get_all.return_value = students
        
        response = test_client.get("/students")
        
        assert response.status_code == 200
        assert response.json() == students
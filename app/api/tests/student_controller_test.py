import pytest
from unittest.mock import AsyncMock, MagicMock
from app.api.controllers.students import StudentController

class TestStudentController:
    @pytest.fixture
    def mock_service(self):
        service = MagicMock()
        service.get_all_students = AsyncMock()
        return service
    
    @pytest.fixture
    def controller(self, mock_service):
        return StudentController(service=mock_service)
    
    @pytest.mark.asyncio
    async def test_get_all_students(self, controller, mock_service):
        
        class MockStudent:
            def __init__(self, id, name, grade, debt):
                self.id = id
                self.name = name
                self.grade = grade
                self.debt = debt
        
        mock_students = [
            MockStudent('A01234354', 'Miguel Mendoza', 10, 100),
            MockStudent('A01234355', 'Fernando Monroy', 10, 0),
            MockStudent('A01234356', 'Regina Cavazos', 5, 50),
            MockStudent('A01234357', 'Jorge Salcedo', 4, 0)
        ]
        
        expected_result = [
            {'matricula': 'A01234354', 'nombre': 'Miguel Mendoza', 'estatus': "Reestructura"},
            {'matricula': 'A01234355', 'nombre': 'Fernando Monroy', 'estatus': "Aprobado"},
            {'matricula': 'A01234356', 'nombre': 'Regina Cavazos', 'estatus': "Expulsado"},
            {'matricula': 'A01234357', 'nombre': 'Jorge Salcedo', 'estatus': "Pendiente"}
        ]
        
        mock_service.get_all_students.return_value = mock_students
        
        result = await controller.get_all()
        
        assert result == expected_result
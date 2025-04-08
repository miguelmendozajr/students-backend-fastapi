from fastapi import APIRouter
from app.api.handlers.students import StudentHttpHandler
from app.api.controllers.students import StudentController

router = APIRouter(prefix="/students", tags=["students"])

# TODO: Missing real db service
student_controller = StudentController()
student_handler = StudentHttpHandler(student_controller)

@router.get("/")
async def get_all_students():
    return await student_handler.get_all_students()
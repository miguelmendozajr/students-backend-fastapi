from fastapi import HTTPException, status
from app.api.controllers.students import StudentController

class StudentHttpHandler:
    def __init__(self, student_controller: StudentController):
        self.student_controller = student_controller

    async def get_all_students(self):
        try:
            students = await self.student_controller.get_all()
            return students
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(error)
            )
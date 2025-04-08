class StudentController:
    def __init__(self, service = None):
        self.service = service
    
    async def get_all(self):
        response = []
        students = await self.service.get_all_students()
        for student in students:
            status = ""
            if student.debt == 0 and student.grade >= 7:
                status = "Aprobado"
            elif student.debt == 0 and student.grade < 7:
                status = "Pendiente"
            elif student.debt > 0 and student.grade >= 7:
                status = "Reestructura"
            else:
                status = "Expulsado"
            
            response.append({
                "matricula": student.id, 
                "nombre": student.name, 
                "estatus": status
            })
            
        return response
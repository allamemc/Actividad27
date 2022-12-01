#cursos:id,nombre, creditos, añosdeestudio
#alumno:id, nombre, email
#matricula:idmatricula, fechamatricula, idalumno, idcurso

class Cursos:
    def __init__(self,id,nombre,creditos,añosdeestudio):
        self.id=id
        self.nombre=nombre
        self.creditos=creditos
        self.añoseestudio=añosdeestudio
    def cursomost(self):
        print(f'curso: {self.nombre} creditos {self.creditos}')
curso1=Cursos(1,'1 Carrera',60,1)
curso2=Cursos(2,'2 Carrera',60,2)


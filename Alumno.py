#Crear estas clases
#Define los atributos, métodos, constructores... que consideres
#necesarios.

#cursos:id,nombre, creditos, añosdeestudio
#alumno:id, nombre, email
#matricula:idmatricula, fechamatricula, idalumno, idcurso

#Necesitamos.
#mostrar la ficha del curso
#mostrar la ficha de alumno
#alumno1 se matricula en un curso
#alumno2 se matricula en dos cursos
#mostrar los datos de matrículo
#reto*:método que muestra las mátriculas realizadas en mi centro

class Alumno:
    def __init__(self,id,nombre,email):
        self.id=id
        self.nombre=nombre
        self.email=email

    def alumnomostr(self):
        print(f'alumno: {self.nombre} email {self.email}')

alumno1=Alumno(1,'jose','jose4@gmail.com')
alumno2=Alumno(2,'maria','maria4@gmail.com')

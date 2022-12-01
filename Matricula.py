#matricula:idmatricula, fechamatricula, idalumno, idcurso
#Necesitamos.
#mostrar la ficha del curso
#mostrar la ficha de alumno
#alumno1 se matricula en un curso
#alumno2 se matricula en dos cursos
#mostrar los datos de matrículo
#reto*:método que muestra las mátriculas realizadas en mi centro

from Cursos import Cursos
from Alumno import Alumno


class Matricula:
    counter = 0
    def __init__(self,idmatricula,fechamatricula,idalumno,idcurso):
        self.idmatricula=idmatricula
        self.fechamatricula=fechamatricula
        self.idalumno=idalumno
        self.idcurso=idcurso
        Matricula.counter += 1 #contador de instancias de objetos cada vez que hagamos una instancia incrementa en uno
    def mostrarmatricula(self):
        print(f'matricula : {self.idalumno} en {self.idcurso}')

curso1=Cursos(1,'1 Ingeniria',60,1)
curso2=Cursos(2,'2 Turismo',60,2)

alumno1=Alumno(1,'jose','jose4@gmail.com')
alumno2=Alumno(2,'maria','maria4@gmail.com')
alumno3=Alumno(3,'juan','juan4@gmail.com')

matri1=Matricula(1,'20/10/2022',alumno1.nombre,curso1.nombre)
matri2=Matricula(2,'22/09/2023',alumno2.nombre,curso1.nombre)
matri3=Matricula(3,'22/05/2024',alumno2.nombre,curso2.nombre)
matri4=Matricula(4,'22/08/2026',alumno3.nombre,curso2.nombre)

matri1.mostrarmatricula()
matri2.mostrarmatricula()
matri3.mostrarmatricula()
curso1.cursomost()
curso2.cursomost()
alumno1.alumnomostr()
alumno2.alumnomostr()

print(f'El total de matriculas es {Matricula.counter}')



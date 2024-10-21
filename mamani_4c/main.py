from mecanico import Mecanico
from vehiculo import Vehiculo

def imprimir_vehiculo(vehi):
    print(f"Patente: {vehi.patente} - Marca: {vehi.marca} - color: {vehi.color} - problemas: {vehi.problemas}")

meca1 = Mecanico("Leidy mamani", 1000000, "Hidraulica", 10)
meca2 = Mecanico("Andrea Díaz", 1000000, "Motor", 6)

vehi1= Vehiculo("AA1122", "Hyundai", "Tucson", "Azul", "No enciende")
vehi2= Vehiculo("BB1122", "Hyundai", "Accent", "Blanco", "Luz delantera izquierda quebrada")
vehi3= Vehiculo("CC1122", "Suzuki", "Jimny", "Negro", "Chocado en puerta del conductor")
vehi4= Vehiculo("DD1122", "Suzuki", "Samurai", "Azul", "Problemas en el encendido")

vehiculos_meca1= [vehi1, vehi2]
vehiculos_meca2= [vehi3, vehi4]

print(f"{meca1.nombre}, con sus {meca1.experiencia} años de experiencia, se especializa en {meca1.especialidad} y su sueldo es ${meca1.salario}")

print(f"{meca2.nombre}, con sus {meca2.experiencia} años de experiencia, se especializa en {meca2.especialidad} y su sueldo es ${meca2.salario}")

print(f"Vehiculos de {meca1.nombre}")
imprimir_vehiculo(vehiculos_meca1[0])
imprimir_vehiculo(vehiculos_meca1[1])

print(f"Vehiculos de {meca2.nombre}")
imprimir_vehiculo(vehiculos_meca2[0])
imprimir_vehiculo(vehiculos_meca2[1])

vehi1.problemas= "Problema electrico"
vehi3.problemas= "Chocado en puerta de copiloto"

print(f"Vehiculos de {meca1.nombre}")
imprimir_vehiculo(vehiculos_meca1[0])
imprimir_vehiculo(vehiculos_meca1[1])

print(f"Vehiculos de {meca2.nombre}")
imprimir_vehiculo(vehiculos_meca2[0])
imprimir_vehiculo(vehiculos_meca2[1])

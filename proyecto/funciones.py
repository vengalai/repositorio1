import json
import random 

def cargar_datos():
    try:
        with open("campus.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"campers": {}, "trainers": {}, "salones": {}}

def guardar_datos(datos):
    with open("campus.json", "w") as f:
        json.dump(datos, f, indent=4)

def registrar_camper(datos):
    print("\n--- REGISTRO DE NUEVO CAMPER ---")
    id_camper = input("Ingrese el número de identificación: ")
    nombre = input("Ingrese el nombre completo: ")
    datos["campers"][id_camper] = {
        "nombre": nombre,
        "estado": "Inscrito",
        "salon": None,
        "ruta": None
    }
    guardar_datos(datos)
    print(f"¡Camper {nombre} registrado exitosamente!")

def asignar_ruta(datos):
    print("\n--- ASIGNACIÓN DE SALONES Y RUTAS ---")
    id_camper = input("Ingrese el ID del camper aprobado: ")
    if id_camper not in datos["campers"]:
        print("Error: El camper no existe.")
        return
    
    if datos:["campers"][id_camper]["estado"] != "Aprobado"
    print(f"Error: El camper está en estado '{datos['campers'][id_camper]['estado']}'. Debe estar 'Aprobado' para matricular.")
    return

print("\nSalones Disponibles (Capacidad máx: 35):")

for nombre, info in datos["salones"].items():
    print(f"- {nombre}: {info['matriculados']}/35 estudiantes.")

disponibles = []

for nombre, info in datos["salones"].items():
    if info["matriculados"] < 35:
        disponibles.append(nombre)

if not disponibles:
    print("Lo sentimos, no hay cupos disponibles en ningún salón.")
    return

seleccion = random.choice(disponibles)
print(f"El sistema ha asignado el salón: {seleccion}")

# Verificación segura
if seleccion in datos["salones"]:
    datos["salones"][seleccion]["matriculados"] += 1

rutas_posibles = ["Java", "NodeJS", "NetCore"]
materia_asignada = random.choice(rutas_posibles)

datos["campers"][id_camper]["salon"] = seleccion
datos["campers"][id_camper]["ruta"] = materia_asignada
datos["campers"][id_camper]["estado"] = "Cursando"

guardar_datos(datos)

print(f"¡Éxito! {datos['campers'][id_camper]['nombre']} asignado a {seleccion} (Ruta: {materia_asignada})")

def listar_campers_por_salon(datos):
        busqueda = input("Ingrese el nombre del salón (Sputnik/Artemis/Apolo): ").capitalize()
        print(f"\n--- Estudiantes en el salón {busqueda} ---")
    
        hay_estudiantes = False

        for id_camper, info in datos["campers"].items():
            if info.get("salon") == busqueda: 
                print(f"ID: {id_camper} - Nombre: {info['nombre']} - Ruta: {info['ruta']}")
            hay_estudiantes = True

        if not hay_estudiantes:
            print("No hay estudiantes matriculados en este salón todavía.")

def registrar_nota_inicial(datos):
    print("\n--- REGISTRO DE PRUEBA DE INGRESO ---")
    id_camper = input("Ingrese el ID del camper: ")

    if id_camper in datos["campers"]:
        try:
            nota_teorica = float(input("Ingrese nota teórica (0-100): "))
            nota_practica = float(input("Ingrese nota práctica (0-100): "))
            promedio = (nota_teorica + nota_practica) / 2

            if promedio >= 60:
                datos["campers"][id_camper]["estado"] = "Aprobado"
                print(f"¡Felicidades! Promedio: {promedio}. Estado: Aprobado.")
            else:
                datos["campers"][id_camper]["estado"] = "Reprobado"
                print(f"Promedio insuficiente: {promedio}. Estado: Reprobado.")
            
            guardar_datos(datos)
        except ValueError:
            print("Error: Ingrese solo números para las notas.")
    else:
        print("El camper no existe en el sistema.")
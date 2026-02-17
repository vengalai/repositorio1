import json

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
    
    if datos["campers"][id_camper]["estado"] != "Aprobado":
        print(f"Error: El camper está en estado '{datos['campers'][id_camper]['estado']}'. Debe estar 'Aprobado' para matricular.")
        return
    print("\nSalones Disponibles (Capacidad máx: 35):")
    for nombre, info in datos["salones"].items():
        print(f"- {nombre}: {info['matriculados']}/35 estudiantes.")
    
    seleccion = input("\nEscriba el nombre del salón (Sputnik/Artemis/Apolo): ").capitalize()

    if seleccion in datos["salones"]:
        if datos["salones"][seleccion]["matriculados"] < 35:
            rutas_asignadas = {
                "Sputnik": "Java",
                "Artemis": "NodeJS",
                "Apolo": "NetCore"
            }
            
            datos["campers"][id_camper]["salon"] = seleccion
            datos["campers"][id_camper]["ruta"] = rutas_asignadas[seleccion]
            datos["campers"][id_camper]["estado"] = "Cursando"
            datos["salones"][seleccion]["matriculados"] += 1
            
            guardar_datos(datos)
            print(f"¡Éxito! {datos['campers'][id_camper]['nombre']} ahora está en {seleccion} viendo {rutas_asignadas[seleccion]}.")
        else:
            print("El salón está lleno. Por favor elija otro.")
    else:
        print("Salón no válido.")
    if id_camper in datos["campers"]:
        print(f"Buscando cupo para {datos['campers'][id_camper]['nombre']}...")
    else:
        print("Camper no encontrado.")
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
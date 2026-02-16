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
        "ruta": None,
        "salon": None
    }
    guardar_datos(datos)
    print(f"¡Camper {nombre} registrado exitosamente!")
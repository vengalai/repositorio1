import funciones

def menu_principal():
    datos = funciones.cargar_datos() 
    
    while True:
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            funciones.registrar_camper(datos) 
        elif opcion == "0":
            print("¡Hasta luego!")
        break
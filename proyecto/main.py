import funciones

def menu_principal():
    datos = funciones.cargar_datos() 
    
    while True:
        print("\n===============================")
        print("   SISTEMA DE GESTIÓN CAMPUS   ")
        print("===============================")
        print("1. Registro de Camper")
        print("2. Registrar Nota (Próximamente)")
        print("3. Gestión de Rutas (Asignación)")
        print("4. Listar campers por salón")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            funciones.registrar_camper(datos)
            
        elif opcion == "2":
            funciones.registrar_nota_inicial(datos) 
            
        elif opcion == "3":
            funciones.asignar_ruta(datos)
        
        elif opcion == "4":
            funciones.listar_campers_por_salon(datos)
            
        elif opcion == "0":
            print("¡Hasta luego!")
            break
            
        else:
            print("\nOpción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
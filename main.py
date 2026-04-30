from interfaz import limpiar_pantalla, pausa
import logica

def ejecutar():
    productos = logica.cargar_datos()
    logica.limpiar_tickets_viejos(7)
    
    while True:
        limpiar_pantalla()
        print("\n>>>> Inventario <<<<\n")
        print("1. Administrar Productos")
        print("2. Consultas y Busqueda")
        print("3. Ventas y stock")
        print("4. Reportes, Herramientas y Backups")
        print("5. Cierre de Caja Diaria")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            while True:
                limpiar_pantalla()
                print("----- ADMINISTRACION -----\n")
                print("1. Agregar producto")
                print("2. Editar producto")
                print("3. Eliminar producto")
                print("0. Volver")
                
                sub = input("\nSeleccione una opcion: ")
                limpiar_pantalla()
                if sub == "1":
                    logica.agregar_producto(productos)
                    logica.guardar_datos(productos)
                    
                elif sub == "2":
                    logica.editar_producto(productos)
                    logica.guardar_datos(productos)
                    
                elif sub == "3":
                    logica.eliminar_producto(productos)
                    logica.guardar_datos(productos)
                    
                elif sub == "0":
                    break
                pausa()
                    
        elif opcion == "2":
            while True:
                limpiar_pantalla()
                print("----- CONSULTAS -----\n")
                print("1. Inventario")
                print("2. Buscar producto")
                print("0. Volver")
                
                sub = input("\nSeleccione una opcion: ")
                limpiar_pantalla()
                if sub == "1":
                    logica.mostrar_inventario(productos)
                    logica.guardar_datos(productos)
                    
                elif sub == "2":
                    logica.buscar_producto(productos)
                    
                elif sub == "0":
                    break
                pausa()
                
                
        elif opcion == "3":
            while True:
                limpiar_pantalla()
                print("----- VENTAS Y STOCK -----\n")
                print("1. Agregar Stock")
                print("2. Registrar Venta")
                print("0. Volver")
                
                sub = input("\nSeleccione una opcion: ")
                limpiar_pantalla()
                if sub == "1":
                    logica.reponer_stock(productos)
                    logica.guardar_datos(productos)
                elif sub == "2":
                    logica.registrar_venta(productos)
                    logica.guardar_datos(productos)
                    
                elif sub == "0":
                    break
                pausa()
                    
        elif opcion == "4":
            while True:
                limpiar_pantalla()
                print("----- REPORTES Y HERRAMIENTAS -----\n")
                print("1. Estadisticas de Productos")
                print("2. Historial de movimientos")
                print("3. Exportar a Excel")
                print("4. Ver ultimo Excel")
                print("5. Crear Backup")
                print("6. Ver Backups")
                print("0. Volver")
                
                sub = input("\nSeleccione una opcion: ")
                limpiar_pantalla()
                if sub == "1":
                    logica.generar_reporte(productos)
                elif sub == "2":
                    logica.mostrar_historial()
                    
                elif sub == "3":
                    logica.exportar_excel(productos)
                    
                elif sub == "4":
                    logica.abrir_excel()
                    
                elif sub == "5":
                    logica.crear_backup(manual=True)
                    
                elif sub == "6":
                    logica.abrir_backups()
                    
                elif sub == "0":
                    break
                pausa()
                
        elif opcion == "5":
                limpiar_pantalla()
                logica.caja_diaria()
                    
        elif opcion == "0":
            print("\nSaliste del Inventario")
            logica.guardar_datos(productos)
            logica.crear_backup(manual=False)
            print("\nBackup Creado\n")
            break
        else:
            print("\nElija una de las opciones disponibles")
        

if __name__ == "__main__":
    ejecutar()
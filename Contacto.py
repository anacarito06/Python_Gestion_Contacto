class Contacto: # Definimos la clase y el nombre de la clase
    def __init__(self, nombre, telefono): #inicializar clase con sus atributos
        self.nombre = nombre
        self.telefono = telefono
    
    def mostrar_menu():
        print("Gesion de contactos")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salid")
    
    contactos = []
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")
        
        if opcion == "5":
            #Salir del programa
            print("Saliendo del programa")
            break
        if opcion == "1":
            #Agregar un nuevo contacto
            nombre = input ("Ingresar el nombre: ")
            telefono = input ("Ingreesa el telefono: ")
            contacto = Contacto(nombre, telefono)
            contactos.append(contacto) # se utiliza para agregar un elemento al final de una lista existente.
            print("Contacto agregado. ")
            
        elif opcion == "2":
            #Mostrar todos los contactos
             for c in contactos:
                 print(f"Nombre: {c.nombre}, Telefono: {c.telefono}")
                
        elif opcion == "3":
            #Buscar un contacto por nombre
            nombre = input("INgresa el nombre a buscar: ")
            encontrado = False
            for c in contactos:
                if c.nombre == nombre:
                    print(f"Nombre: {c.nombre}, Telefono: {c.telefono}")
                    encontrado = True
                    break
            if not encontrado:
                print("Contacto no encontrado. ")

        elif opcion == "4":
            #Eliminar un contacto por nombre
            nombre = input("Ingresa el nombre a eliminar: ")
            for c in contactos:
                if c.nombre == nombre:
                    contactos.remove(c)
                    print("Contacto eliminado")
                    break
        else:
            #Manejar opcion no valido
            print("Opcion no valido. Intentalo de nuevo")

           
            

    
        
        
    
    

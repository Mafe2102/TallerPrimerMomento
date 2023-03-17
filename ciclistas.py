opcion=5
ciclistas=[]
print("**GIRO DE ITALIA**")
print("*Ultima Prueba Crono*")
print("1: Ingresar datos del Ciclista")
print("2: Mostrar Tabla de Posiciones de la Prueba")
print("3: Corregir Tiempo")
print("4: Retirar de la Tabla")
print("0: Salir")
while opcion !=0:
    opcion=int(input("Ingresa la opcion deseada: "))
    if opcion==1:
        ciclista={}
        ciclista["codigo"]=int(input("Digita el codigo del ciclista: "))
        ciclista["nombre"]=input("Digita el nombre del ciclista: ")
        ciclista["edad"]=int(input("Digita la edad del ciclista: "))
        ciclista["pais"]=input("Digita el pais del ciclista: ")
        ciclista["equipo"]=input("Digita el equipo del ciclista: ")
        ciclista["tiempo"]=int(input("Digita el tiempo del ciclista(minutos): "))
        print("Ciclista ingresado con exito")
        ciclistas.append(ciclista)
    elif opcion==2:
        print(ciclistas)
    elif opcion==3:
        ciclistaABuscar=int(input("Digita el codigo del ciclista a buscar: "))
        for ciclistaSeleccionado in ciclistas:
            if ciclistaSeleccionado["codigo"] == ciclistaABuscar:
                ciclistaSeleccionado["tiempo"]=float(input("Ingresa el nuevo tiempo: "))
                print("Tiempo actualizado con exito")
            else:
                print("No se encontró el ciclista")
    elif opcion==4:
        ciclistaARetirar=int(input("Digita el codigo del ciclista a retirar: "))
        for ciclistaSeleccionado in ciclistas:
            if ciclistaSeleccionado["codigo"] == ciclistaARetirar:
                ciclistas.remove(ciclistaSeleccionado)
                print("Dato eliminado con exito")
            else:
                print("No se encontró el ciclista")

#  La reina Cersei Lannister necesita administrar sus fondos
# almacenados en el banco de hierro de la isla de bravos. La
# reina tiene 10 cuentas con fondos diferentes. Cada cuenta
# tiene un numero de cuenta y un saldo. Elabore un programa
# que permita recibir el saldo de las 10 cuentas y al
# finalizar muestre por consola las cuentas de mayor a menor saldo +1.0

controlador=10
cuentas=[] 
lista=0
numerosOrdenados=0
print("***CUENTAS BANCARIAS")
while (lista < controlador):
    cuenta = int(input("Ingresa el saldo de tu cuenta: "))
    cuentas.append(cuenta)
    lista += 1

numerosOrdenados = sorted(cuentas, reverse=True)
print("Saldo cuenta")
for f in numerosOrdenados:
    print(f)
        
else:
    print("Fin del programa")
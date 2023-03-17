numeros = []
multiplo2 =[]
miltiplo3 = []

numero = {}
numero ["numero1"] = int(input("Digite numero: "))
numero ["numero2"] = int(input("Digite numero: "))
numero ["numero3"] = int(input("Digite numero: "))
numero ["numero4"] = int(input("Digite numero: "))
numero ["numero5"] = int(input("Digite numero: "))


if numero % 2 == 0:
    multiplo2 = [numero]
    
if numero % 3 == 0:
    multiplo3 = [numero]
    
print(f"Los multiplos de 2 son: {multiplo2}")
print(f"Los multiplos de 3 son: {multiplo3}")
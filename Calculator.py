
# creando operaciones y variables
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    return a / b


print("Please, select your operation:")
print("1 - Suma")
print("2 - Resta")
print("3 - Multiplicacion")
print("4 - Division")

# creando aplicativo
while True:
    choice = input("Por favor, Ingrese una opcion : (1 | 2 | 3 | 4): ")
    if choice in ('1', '2', '3', '4'):
        numero1 = float(input("Por favor, Ingrese el primer dato : "))
        numero2 = float(input("Por favor, Ingrese el segundo dato : "))
        if choice == '1':
            print(f"{numero1} + {numero2} = ", suma(numero1, numero2))
        elif choice == '2':
            print(f"{numero1} - {numero2} = ", resta(numero1, numero2))
        elif choice == '3':
            print(f"{numero1} * {numero2} = ", multiplicacion(numero1, numero2))
        elif choice == '4':
            print(f"{numero1} / {numero2} = ", division(numero1, numero2))

    else:
        print("Su opcion no es valida")

    # preguntando al usuario si desea continuar

    keep_running = input("Desea continuar ? Si o No?")
    if keep_running in ('Si', 's', 'SI', 'S', 'si'):
        continue
    else:
        break


 

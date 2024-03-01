#Saludo personalizado

def saludar():
    return input('Escriba su nombre: ')

nombre = saludar()
print(f'Hola {nombre}, ¿cómo estás?')





def oper_arismet():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    operacion = input("Ingrese la operación deseada (suma, resta, multiplicacion, division): ")

    if operacion == "suma":
        resultado = num1 + num2
    elif operacion == "resta":
        resultado = num1 - num2
    elif operacion == "multiplicacion":
        resultado = num1 * num2
    elif operacion == "division":
        if num2 == 0:
            print('ERROR')
            return None
        resultado = num1 / num2
    else:
        print('ingrese una operacion valida')
        return None


    print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")
    return resultado


resultado = oper_arismet()



def check_name(x):
    if isinstance(x,str):
        if x.lower() == "thomas":
            return "beautiful name btw"
        else:
            return "ugly name btw"
    else:
        return "not a valid name"


print(check_name(nombre))

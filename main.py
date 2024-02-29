#Saludo personalizado

def saludar():
    return input('Escriba su nombre: ')

nombre = saludar()
print(f'Hola {nombre}, ¿cómo estás?')


def check_name(x):
    if isinstance(x,str):
        if x.lower() == "thomas":
            return "beautiful name btw"
        else:
            return "ugly name btw"
    else:
        return "not a valid name"


print(check_name(nombre))

from persona import Persona


def esMayorDeEdad(edad: int):
    if edad >= 18:
        print('Es mayor de edad')
    else:
        print('No es mayor de edad')


def main():
    user_choice = input('Ingrese su nombre: ')
    age = int(input('ingrese su edad: '))

    print('Su informacion es:')
    print(user_choice)
    print(age)

    print(esMayorDeEdad(age))



main()

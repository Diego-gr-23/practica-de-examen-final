from cuenta import Cuenta

cuenta_total = Cuenta


def saldo(cuenta):
    if cuenta > 0:
        saldo_total = cuenta
        return saldo_total
    elif cuenta <= 0:
        print('Saldo insuficiente')


def main():
    saldo_total = 0
    while True:
        user_choice = int(input('Elija una opcion: \n'
                                '1 - Mostrar saldo total \n'
                                '2 - Ingresar saldo \n'
                                '3 - rertirar saldo \n'))

        if user_choice == 1:
            print('Saldo total')
            print(saldo(saldo_total))
        elif user_choice == 2:
            choice = input('Ingrese su nombre:')
            ingresar = int(input('Ingrese la cantidad que desea imgresar:'))
            saldo_total += ingresar
            print(f'Gracias senior/a {choice}')
        else:
            retirar = int(input('Cuanto desea retirar: '))
            saldo_total -= retirar
            print('Usted retiro:')
            print(saldo(saldo_total))


main()

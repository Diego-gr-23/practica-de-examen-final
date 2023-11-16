from queue import Queue
from musica import Musica

canciones = Queue()


song1 = Musica('Ride')
canciones.push(song1)
song3 = Musica('Surround Sound')
canciones.push(song3)
song4 = Musica('Un Verano sin ti')
canciones.push(song4)
song5 = Musica('Toda')
canciones.push(song5)
song6 = Musica('Low Life')
canciones.push(song6)


def main():
    while True:
        user_choice = int(input('Ingrese una opcion \n'
                                '1 - Ingresar canciones \n'
                                '2 - Ver lista en cola \n'
                                '3 - Quitar cancion en lista \n'
                                '4 - Salir del reproductor \n'))
        if user_choice == 4:
            break
        else:
            if user_choice == 1:
                song = input('Ingrese el nombre de una cancion: ')
                musica = Musica(song)
                canciones.push(musica)
            elif user_choice == 2:
                print('Las canciones que estan en cola son:')
                print(canciones.transversal())

            elif user_choice == 3:
                print('La cancion que quito de la lista es:')
                print(canciones.pop())


main()

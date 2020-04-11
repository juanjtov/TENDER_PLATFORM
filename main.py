#-*- coding: utf-8 -*-

def run():
    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [m]ontar licitación
            [l]icitar
            [s]alir
        ''')).lower()

        if command == 'm':
            print('Voy a montar licitación')

        elif command == 'l':
            print('voy a licitar')

        elif command == 's':
            break
        else:
            print('El comando seleccionado no existe')

if __name__ == "__main__":
    run()
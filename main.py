#-*- coding: utf-8 -*-
import csv

class Empresas:

    def __init__(self, name, phone, email, city):

        self._name = name
        self._phone = phone
        self._email = email
        self._city = city

class TenderPlat:

    def __init__(self):
        self._companies = []
        
    def add(self, name, phone, email, city): #Método para crear empresas

        empresa = Empresas(name, phone, email, city) #Instancia de la clase Empresas

        self._companies.append(empresa)    
        self._save()

        print('Su empresa ha sido agregada exitosamente')

    def show_comp(self):
        for empresa in self._companies:
            self._print_companies(empresa)

    #Este método es privado porque solo lo voy a llamar dentro de la clase
    def _print_companies(self, empresa):
        print('*********************************')
        print('Nomre de la compañía: {}'.format(empresa._name))
        print('Télefono: {}'.format(empresa._phone))
        print('Email: {}'.format(empresa._email))
        print('Ciudad de la licitación: {}'.format(empresa._city))

    
    #Creo esa función para almacenar los datos en disco duro
    #Así no se borran cada vez que ejecuto el archivo
    #Sin embargo acá solo escribo sobre el archivo
    def _save(self):
        with open('companies.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email', 'city'))

            for comp in self._companies:
                writer.writerow((comp._name, comp._phone, comp._email, comp._city))

        

def run():

    tender_plat = TenderPlat()


    #A través de la siguiente instrucción leo el archivo  e inmediatamente
    #me quedan listos para usarlos
    with open('companies.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            #Voy excluir la primera fila que es donde está el encabezado
            if idx == 0:
                continue
            else:
                tender_plat.add(row[0], row[1], row[2], row[3])

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [m]ontar licitación
            [l]icitar
            [lis]tar empresas existentes
            [s]alir
        ''')).lower()

        if command == 'm':
            print('Generando empresa para montar licitación')
            name = str(input('Ingrese el nombre de la empresa: '))
            phone = str(input('Ingrese número de télefono de la empresa: '))
            email = str(input('Ingrese email de la empresa: '))
            city = str(input('Ciudad donde requiere el servicio de licitación: '))

            tender_plat.add(name, phone, email, city)

        elif command == 'l':
            print('Mostrando Procesos')

        elif command == 'lis':
            print('Estas son las empresas existentes')
            tender_plat.show_comp()

        elif command == 's':
            break
        else:
            print('El comando seleccionado no existe')

if __name__ == "__main__":
    run()
#-*- coding: utf-8 -*-

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



def run():

    tender_plat = TenderPlat()
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
            print('voy a licitar')

        elif command == 'lis':
            print('Estas son las empresas existentes')
            tender_plat.show_comp()

        elif command == 's':
            break
        else:
            print('El comando seleccionado no existe')

if __name__ == "__main__":
    run()
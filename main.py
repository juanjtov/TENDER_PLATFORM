#-*- coding: utf-8 -*-
import csv

class Empresas:

    def __init__(self, name, phone, email, city):

        self._name = name
        self._phone = phone
        self._email = email
        self._city = city

class Processes:

    def __init__(self, proc_name, categoria, ciudad, descripcion):

        self._proc_name = proc_name
        self._categoria = categoria
        self._ciudad = ciudad
        self._descripcion = descripcion

class TenderPlat:

    def __init__(self):
        self._companies = []
        self._process = []
        
    def add(self, name, phone, email, city): #Método para crear empresas

        empresa = Empresas(name, phone, email, city) #Instancia de la clase Empresas

        self._companies.append(empresa)    
        self._save()

        print('Su empresa ha sido agregada exitosamente')

    def add_process(self, proc_name, categoria, ciudad, descripcion):

        proceso = Processes(proc_name, categoria, ciudad, descripcion)

        self._process.append(proceso)

        print('Se agrego proceso')
        


    def show_comp(self):
        for empresa in self._companies:
            self._print_companies(empresa)

    def show_process(self):
        for proceso in self._process:
            self._print_procesos(proceso)

    #Este método es privado porque solo lo voy a llamar dentro de la clase
    def _print_companies(self, empresa):
        print('*********************************')
        print('Nomre de la compañía: {}'.format(empresa._name))
        print('Télefono: {}'.format(empresa._phone))
        print('Email: {}'.format(empresa._email))
        print('Ciudad de la licitación: {}'.format(empresa._city))

    def _print_procesos(self, proceso):
        print('*********************************')
        print('Nombre del proceso: {}'.format(proceso._proc_name))
        print('Télefono: {}'.format(proceso._categoria))
        print('Email: {}'.format(proceso._ciudad))
        print('Ciudad de la licitación: {}'.format(proceso._descripcion))




    
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
            [lise]Listar empresas existentes
            [lispro]Listar procesos existentes
            [s]alir
        ''')).lower()

        if command == 'm':
            print('Generando empresa para montar licitación')
            name = str(input('Ingrese el nombre de la empresa: '))
            phone = str(input('Ingrese número de télefono de la empresa: '))
            email = str(input('Ingrese email de la empresa: '))
            city = str(input('Ciudad donde está ubicada la empresa: '))

            tender_plat.add(name, phone, email, city)

            process = str(input('''
                ¿Desea adicionar proceso de licitación?

                [s]i
                [n]o
            ''')).lower()

            if process == 's':
                proc_name = str(input('Nombre del proceso de licitación: '))
                categoria = str(input('Categoria del proceso de licitación: '))
                ciudad = str(input('Ciudad donde se requiere el producto o serivicio: '))
                descripcion = str(input('Actividad a realizar: '))

                tender_plat.add_process(proc_name, categoria, ciudad, descripcion)

            elif process == 'n':
                print('No se agrego ningún proceso ha esta empresa')

            else:
                print('Comando no encontrado')

                
                

        elif command == 'lispro':
            print('Mostrando Procesos Existentes')
            tender_plat.show_process()


        elif command == 'lise':
            print('Estas son las empresas existentes')
            tender_plat.show_comp()

        elif command == 's':
            break
        else:
            print('El comando seleccionado no existe')

if __name__ == "__main__":
    run()
'''--- Librerias de Python ---'''
from os import system

import time #(Libreria de Python para Linux)

'''--- Variable Global---'''
nombre_archivo = "basedatos.txt"
nota_archivo = "notas.txt"

'''--- Clases --- *(Recuerda que para hacer uso de estas deben estar puestas antes
                    de ser llamadas)'''

class methods():
    def _menu_principal(opc_main):
        match opc_main:
            case 1:
                return personal.alumnos()
            case 2:
                return personal.notas()
            case 3:
                return personal.reportes()
            case 4:
                system('clear') #Comando para limpiar el terminal en LINUX
                #system('cls') Comando para limpiar el terminal en Windows
                print('¡Gracias por usar nuestro programa!')
                return
            case _:
                system('clear') #Comando para limpiar el terminal en LINUX
                #system('cls') Comando para limpiar el terminal en Windows
                print('¡La opcion ingresada es invalida! Pulse cualquier tecla para intentar nuevamente', end="")
                input()
                return main_menu()
            
    def _menu_alumnos(opc_alumnos):
        match opc_alumnos:
            case 1:
                return alumnos.cargar_alumnos()
            case 2:
                return personal.menu_modificar_alumno()
            case 3:
                return alumnos.eliminar_alumnos()
            case 4:
                return main_menu()
            case _:
                system('clear') #Comando para limpiar el terminal en LINUX
                #system('cls') Comando para limpiar el terminal en Windows
                print('¡La opcion ingresada es invalida! Pulse enter para intentar nuevamente', end="")
                input()
                return personal.alumnos()
            
    def _menu_notas(opc_notas):
        match opc_notas:
            case 1:
                return notas.cargar_nota()
            case 2:
                return personal.modificar_notas()
            case 3:
                return personal.eliminar_notas()
            case 4:
                return main_menu()
            case _:
                system('clear') #Comando para limpiar el terminal en LINUX
                #system('cls') Comando para limpiar el terminal en Windows
                print('¡La opcion ingresada es invalida! Pulse enter para intentar nuevamente', end="")
                input()
                return personal.notas()
            
    def _menu_reportes(opc_notas):
        match opc_notas:
            case 1:
                return personal.alumnos()
            case 2:
                return personal.notas()
            case 3:
                main_menu()
                return
            case _:
                system('clear') #Comando para limpiar el terminal en LINUX
                #system('cls') Comando para limpiar el terminal en Windows
                print('¡La opcion ingresada es invalida! Pulse enter para intentar nuevamente', end="")
                input()
                return personal.reportes()

    def _menu_mod_alumnos(opc_notas):
        match opc_notas:
            case 1:
                return alumnos.modificar_alumnos()
            case 2:
                return personal.notas()
            case 3:
                return personal.reportes()
            case 4:
                main_menu()
                return
            case _:
                system('clear') #Comando para limpiar el terminal en LINUX
                #system('cls') Comando para limpiar el terminal en Windows
                print('¡La opcion ingresada es invalida! Pulse enter para intentar nuevamente', end="")
                input()
                return personal.menu_modificar_alumno()


class rwu_files():
    def write_alumno(nombre_archivo, list):
        with open(nombre_archivo, "a") as archivo:
            for line in list:
                linea = ",".join(str(dato) for dato in line)
                archivo.write(linea + "\n")
    
    def write_notas(nombre_archivo, list):
        with open(nombre_archivo, "a") as archivo:
            for line in list:
                linea = ",".join(str(dato) for dato in line)
                archivo.write(linea + "\n")


class personal():
    def alumnos():
        system('clear') #Comando para limpiar el terminal en LINUX
        #system('cls') Comando para limpiar el terminal en Windows
        print(f''' 
               Carga Estudiantil
            UNEFA - Nucleo Caracas
        Ing. de Sistemas - 6to Semestre
                 MENU ALUMNOS

    1. Ingresar Alumno
    2. Modificar Alumno
    3. Eliminar Alumno
    4. Regresar al menú principal
        
Ingrese una opcion y pulse enter para continuar: ''', end="")
        try:
            opc_alumnos = int(input())
        except ValueError:
            system('clear')
            print('¡La opcion ingresada es invalida! Pulse enter para intentar nuevamente', end="")
            input()
            return personal.alumnos()
        methods._menu_alumnos(opc_alumnos)
        
    def notas():
        system('clear') #Comando para limpiar el terminal en LINUX
        #system('cls') Comando para limpiar el terminal en Windows
        print(f''' 
               Carga Estudiantil
            UNEFA - Nucleo Caracas
        Ing. de Sistemas - 6to Semestre
                 MENU NOTAS

    1. Cargar Nota
    2. Modificar Nota
    3. Eliminar Nota
    4. Regresar al menu principal
        
Ingrese una opcion y pulse enter para continuar: ''', end="")
        try:
            opc_notas = int(input())
        except ValueError:
            system('clear')
            print('¡La opcion ingresada es invalida! Pulse enter para intentar nuevamente', end="")
            input()
            return personal.notas()
        methods._menu_notas(opc_notas)

    def reportes():
        system('clear') #Comando para limpiar el terminal en LINUX
        #system('cls') Comando para limpiar el terminal en Windows
        print(f''' 
               Carga Estudiantil
            UNEFA - Nucleo Caracas
        Ing. de Sistemas - 6to Semestre
                 MENU REPORTES

    1. Imprimir Notas por Alumno
    2. Imprimir Notas por Salon
    3. Salir
        
Ingrese una opcion y pulse enter para continuar: ''', end="")
        try:
            opc_reportes = int(input())
        except ValueError:
            system('clear') #Comando para limpiar el terminal en LINUX
            #system('cls') Comando para limpiar el terminal en Windows
            print('¡La opcion ingresada es invalida! Pulse enter para intentar nuevamente', end="")
            input()
            return personal.reportes()
        methods._menu_reportes(opc_reportes)

    def menu_modificar_alumno():
        system('clear') #Comando para limpiar el terminal en LINUX
        #system('cls') Comando para limpiar el terminal en Windows
        print(f''' 
                Carga Estudiantil
              UNEFA - Nucleo Caracas
                 MODIFICAR ALUMNO

    1. Modificar Nombre
    2. Modificar Apellido
    3. Modificar Materia Inscrita
        
Ingrese una opcion y pulse enter para continuar: ''', end="")
        try:
            opc_mod = int(input())
        except ValueError:
            system('clear')
            print('¡La opcion ingresada es invalida! Pulse enter para intentar nuevamente', end="")
            input()
            return personal.menu_modificar_alumno()
        return methods._menu_mod_alumnos(opc_mod)

class alumnos():
    def cargar_alumnos():
        vals_alumno = []
        system('clear') #Comando para limpiar el terminal en LINUX
        #system('cls') Comando para limpiar el terminal en Windows
        print('''
               Carga Estudiantil
            UNEFA - Nucleo Caracas

  Ingrese el numero de cedula del Estudiante: ''', end='')
        try:
            identification_card = int(input())
            identification_card = str(identification_card)
            if len(identification_card) > 9:
                raise
            system('clear') #Comando para limpiar el terminal en LINUX
            #system('cls') Comando para limpiar el terminal en Windows
            print('La cédula del estudiante a sido cargado con exito!', end="")
            time.sleep(2)
            system('clear') 
        except:
            system('clear') #Comando para limpiar el terminal en LINUX
            #system('cls') Comando para limpiar el terminal en Windows
            print('La cédula no puede ser mayor a 9 digitos, por favor, ingrese un numero en el rango permitido.', end="")
            time.sleep(2)
            return alumnos.cargar_alumnos()#Comando para limpiar el terminal en LINUX
            #system('cls') Comando para limpiar el terminal en Windows
        print('''
            Carga Estudiantil
          UNEFA - Nucleo Caracas

     Ingrese el nombre del Estudiante: ''', end='')
        try:
            name = input()
            system('clear') #Comando para limpiar el terminal en LINUX
                #system('cls') Comando para limpiar el terminal en Windows
            print('¡El nombre del estudiante se ha registrado correctamente!', end="")
            time.sleep(2)
        except:
            system('clear') 
            print('¡El nombre del estudiante que a ingresado, no puede tener numeros o carecteres especiales!', end="")
            time.sleep(2)
            system('clear')
        system('clear')
        print('''
            Carga Estudiantil
          UNEFA - Nucleo Caracas

     Ingrese el apellido del Estudiante: ''', end='')
        last_name = str(input())
        if last_name:
            system('clear') #Comando para limpiar el terminal en LINUX
            #system('cls') Comando para limpiar el terminal en Windows
            print('¡El apellido del estudiante a sido cargado con exito!', end="")
            time.sleep(2)
        system('clear') #Comando para limpiar el terminal en LINUX
        #system('cls') Comando para limpiar el terminal en Windows
        print('''
            Carga Estudiantil
          UNEFA - Nucleo Caracas

Ingrese la materia que el estudiante va a cursar: ''', end='')
        matery = str(input())
        if matery:
            system('clear') #Comando para limpiar el terminal en LINUX
            #system('cls') Comando para limpiar el terminal en Windows
            print('¡La materia a sido cargada con exito!', end="")
            time.sleep(2)
        system('clear') #Comando para limpiar el terminal en LINUX
            #system('cls') Comando para limpiar el terminal en Windows
        opc_charge = input('¿Desea ingresar otro estudiante? (S/N) ')
        if opc_charge.upper() == 'S':
            vals_alumno.append([identification_card, name, last_name, matery])
            rwu_files.write_alumno(nombre_archivo, vals_alumno)
            alumnos.cargar_alumnos()
        else:
            vals_alumno.append([identification_card, name, last_name, matery])
            rwu_files.write_alumno(nombre_archivo, vals_alumno)
            vals_alumno = []
            personal.alumnos()

    def modificar_alumnos():
        try:
            system('clear') #Comando para limpiar el terminal en LINUX
            with open(nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
                print('''
            Carga Estudiantil
          UNEFA - Nucleo Caracas
          MODIFICAR NOMBRE ALUMNO
        Ingrese la cédula: ''', end='')
                cedula = input()
                for i, linea in enumerate(lineas):
                    partes = linea.strip().split(',')
                    if cedula == partes[0]:
                        system('clear') #Comando para limpiar el terminal en LINUX
                        #system('cls') Comando para limpiar el terminal en Windows
                        print('''
            Carga Estudiantil
          UNEFA - Nucleo Caracas
          MODIFICAR NOMBRE ALUMNO

        Ingrese el nuevo nombre: ''', end='')
                        nombre_nuevo = input()
                        partes[1] = nombre_nuevo
                        lineas[i] = ','.join(partes) + '\n'
                        break
            with open(nombre_archivo, 'w') as archivo:
                archivo.writelines(lineas)
                time.sleep(2)
                system('clear') #Comando para limpiar el terminal en LINUX
                #system('cls') Comando para limpiar el terminal en Windows
                print('El nombre se a modificado satisfactoriamente')
        except:
            system('clear') #Comando para limpiar el terminal en LINUX
            #system('cls') Comando para limpiar el terminal en Windows
            print('La cedula ingresada, no se encuentra. Por favor, intente nuevamente.', end="")
            time.sleep(2)
            return alumnos.modificar_alumnos()
        time.sleep(2)
        system('clear') #Comando para limpiar el terminal en LINUX
        #system('cls') Comando para limpiar el terminal en Windows
        opc_alumno = input('¿Desea modificar otro estudiante? (S/N) ')
        if opc_alumno.upper() == 'S':
            personal.menu_modificar_alumno()
        else:
            personal.alumnos()
        
    def eliminar_alumnos():
        try:
            system('clear') #Comando para limpiar el terminal en LINUX
            with open(nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
                print('''
                Carga Estudiantil
            UNEFA - Nucleo Caracas
                ELIMINAR ALUMNO

            Ingrese la cedula: ''', end='')
                cedula = input()
                lineas = [linea for linea in lineas if not linea.startswith(cedula)]
            with open(nombre_archivo, 'w') as archivo:
                archivo.writelines(lineas)
            time.sleep(2)
            system('clear') #Comando para limpiar el terminal en LINUX
            #system('cls') Comando para limpiar el terminal en Windows
            print('El estudiante se ha eliminado satisfactoriamente')
        except:
            system('clear') #Comando para limpiar el terminal en LINUX
            #system('cls') Comando para limpiar el terminal en Windows
            print('La cedula ingresada, no se encuentra. Por favor, intente nuevamente.', end="")
            time.sleep(2)
            return alumnos.modificar_alumnos()
        time.sleep(2)
        system('clear') #Comando para limpiar el terminal en LINUX
        #system('cls') Comando para limpiar el terminal en Windows
        opc_alumno = input('¿Desea eliminar otro estudiante? (S/N) ')
        if opc_alumno.upper() == 'S':
            personal.eliminar_alumnos()
        else:
            personal.alumnos()


class notas():
    def cargar_nota():
        vals_notas = []
        system('clear') #Comando para limpiar el terminal en LINUX
        #system('cls') Comando para limpiar el terminal en Windows
        print(f''' 
                Carga Estudiantil
              UNEFA - Nucleo Caracas
                  CARGAR NOTAS

    Ingrese la cedula del estudiante: ''', end="")
        cedula = input()

        system('clear') #Comando para limpiar el terminal en LINUX
        #system('cls') Comando para limpiar el terminal en Windows
        print(f''' 
                Carga Estudiantil
              UNEFA - Nucleo Caracas
                  CARGAR NOTAS

    Ingrese la nota del primer corte: ''', end="")
        nota = input()

        system('clear') #Comando para limpiar el terminal en LINUX
        #system('cls') Comando para limpiar el terminal en Windows
        print(f''' 
                Carga Estudiantil
              UNEFA - Nucleo Caracas
                  CARGAR NOTAS

    Ingrese la nota del segundo corte: ''', end="")
        nota_2 = input()
        system('clear') #Comando para limpiar el terminal en LINUX
        #system('cls') Comando para limpiar el terminal en Windows
        print(f''' 
                Carga Estudiantil
              UNEFA - Nucleo Caracas
                  CARGAR NOTAS

    Ingrese la nota del tercer corte: ''', end="")
        nota_3 = input()
        system('clear') #Comando para limpiar el terminal en LINUX
        #system('cls') Comando para limpiar el terminal en Windows
        print(f''' 
                Carga Estudiantil
              UNEFA - Nucleo Caracas
                  CARGAR NOTAS

    Ingrese la nota del cuarto corte: ''', end="")
        nota_4 = input()
        time.sleep(2)
        system('clear') #Comando para limpiar el terminal en LINUX
        #system('cls') Comando para limpiar el terminal en Windows
        opc_charge = input('¿Desea cargar la nota a otro estudiante? (S/N) ')
        if opc_charge.upper() == 'S':
            vals_notas.append([cedula, nota, nota_2, nota_3, nota_4])
            rwu_files.write_notas(nota_archivo, vals_notas)
            notas.cargar_nota()
        else:
            vals_notas.append([cedula, nota, nota_2, nota_3, nota_4])
            rwu_files.write_notas(nota_archivo, vals_notas)
            vals_notas = []
            personal.notas()






'''--- Comienzo del programa ---'''
def main_menu():
    system('clear') #Comando para limpiar el terminal en LINUX
    #system('cls') Comando para limpiar el terminal en Windows
    print(f''' 
               Carga Estudiantil
            UNEFA - Nucleo Caracas
        Ing. de Sistemas - 6to Semestre
                MENU PRINCIPAL
            
    1. Alumnos
    2. Notas
    3. Reportes
    4. Salir
        
Ingrese una opcion y pulse enter para continuar: ''', end="")
    try:
        opc_main = int(input())
    except ValueError:
        system('clear')
        print('¡La opcion ingresada es invalida! Pulse enter para intentar nuevamente', end="")
        input()
        return main_menu()
    methods._menu_principal(opc_main)
main_menu()


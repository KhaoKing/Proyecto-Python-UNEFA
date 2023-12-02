'''--- Librerias de Python ---'''
from os import system #(Libreria de Python para Linux)

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
        opc_alumnos = int(input())

    def notas():
        system('clear') #Comando para limpiar el terminal en LINUX
        #system('cls') Comando para limpiar el terminal en Windows
        print(f''' 
               Carga Estudiantil
            UNEFA - Nucleo Caracas
        Ing. de Sistemas - 6to Semestre

    1. Alumnos
    2. Notas
    3. Reportes
    4. Salir
        
Ingrese una opcion y pulse enter para continuar: ''', end="")
        opc_notas = int(input())

    def reportes():
        system('clear') #Comando para limpiar el terminal en LINUX
        #system('cls') Comando para limpiar el terminal en Windows
        print(f''' 
               Carga Estudiantil
            UNEFA - Nucleo Caracas
        Ing. de Sistemas - 6to Semestre

    1. Alumnos
    2. Notas
    3. Reportes
    4. Salir
        
Ingrese una opcion y pulse enter para continuar: ''', end="")
        opc_reportes = int(input())

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
    opc_main = int(input())
    methods._menu_principal(opc_main)
main_menu()


#código de python


tabla = [] #para guardar los IMC calculados anteriormente 

while True:
    print('Bienvenido a tu calculadora de IMC\n')#menú interactivo
    print('1. Iniciar a calcular tu IMC\n')
    print('2. Accede a tu tabla de datos\n')
    print('3. Salir del programa\n')

    
    opcion = int(input('Selecciona tu opción: '))#seleccion de opciones

    if opcion == 1:
        def calcula_imc(peso, altura):#función en el que se hace el calculo del IMC
            imc = peso / (altura ** 2)
            return imc
        peso = float(input('Ingresa tu peso en kilogramos: \n'))
        altura = float(input('Ingresa tu altura en metros: \n'))
        dato3 = int(input('Ingresa tu edad: \n'))               #agregado para solicitar edad y dar consejeria
        if dato3 >= 65:
                        print('Tu indice de masa corporal ideal es entre 24-29, si tu indice de masa corporal es alto te recomendamos llevar una dieta balanceada, aunque no te recomendamos que inicies repentinamente, inicia poco a poco. Tambien te recomendamos hacer actividad física, tomar suficiente agua y dormir lo necesario.\n')
                        print('Si tu indice de masa corporal es bajo te recomendamos comer mas proteínas, comer mas calorias, incluir mas carbohidratos en tu vida, pero siempre teniendo cuidado de no comer alimentos altamente procesados\n')
        elif dato3 >= 55 and dato3 <= 64:
                        print('Tu indice de masa corporal ideal es entre 23-28, si tu indice de masa corporal es alto te    recomendamos llevar una dieta balanceada, aunque no te recomendamos que inicies repentinamente, inicia poco a poco. Tambien te recomendamos hacer actividad física, tomar suficiente agua y dormir lo necesario.')
                        print('Si tu indice de masa corporal es bajo te recomendamos comer mas proteínas, comer mas calorias, incluir mas carbohidratos en tu vida, pero siempre teniendo cuidado de no comer alimentos altamente procesados')
        elif dato3 >= 45 and dato3 <= 54:
                        print('Tu indice de masa corporal ideal es entre 22-27, si tu indice de masa corporal es alto te recomendamos llevar una dieta balanceada, aunque no te recomendamos que inicies repentinamente, inicia poco a poco. Tambien te recomendamos hacer actividad física, tomar suficiente agua y dormir lo necesario.')
                        print('Si tu indice de masa corporal es bajo te recomendamos comer mas proteínas, comer mas calorias, incluir mas carbohidratos en tu vida, pero siempre teniendo cuidado de no comer alimentos altamente procesados')
        elif dato3 >= 35 and dato3 <= 44:
                        print('Tu indice de masa corporal ideal es entre 21-26, si tu indice de masa corporal es alto te recomendamos llevar una dieta balanceada, aunque no te recomendamos que inicies repentinamente, inicia poco a poco. Tambien te recomendamos hacer actividad física, tomar suficiente agua y dormir lo necesario.')
                        print('Si tu indice de masa corporal es bajo te recomendamos comer mas proteínas, comer mas calorias, incluir mas carbohidratos en tu vida, pero siempre teniendo cuidado de no comer alimentos altamente procesados')
        elif dato3 >= 25 and dato3 <= 34:
                        print('Tu indice de masa corporal ideal es entre 20-25, si tu indice de masa corporal es alto te recomendamos llevar una dieta balanceada, aunque no te recomendamos que inicies repentinamente, inicia poco a poco. Tambien te recomendamos hacer actividad física, tomar suficiente agua y dormir lo necesario.')
                        print('Si tu indice de masa corporal es bajo te recomendamos comer mas proteínas, comer mas calorias, incluir mas carbohidratos en tu vida, pero siempre teniendo cuidado de no comer alimentos altamente procesados')
        elif dato3 >=18 and dato3 <= 24:
                        print('Tu indice de masa corporal ideal es entre 19-24, si tu indice de masa corporal es alto te    recomendamos llevar una dieta balanceada, aunque no te recomendamos que inicies repentinamente, inicia poco a poco. Tambien te recomendamos hacer actividad física, tomar suficiente agua y dormir lo necesario.')
                        print('Si tu indice de masa corporal es bajo te recomendamos comer mas proteínas, comer mas calorias, incluir mas carbohidratos en tu vida, pero siempre teniendo cuidado de no comer alimentos altamente procesados') 
        elif dato3 <18:
                        print('Tu indice de masa corporal ideal es entre 14-20, si tu indice de masa corporal es alto te    recomendamos llevar una dieta balanceada, aunque no te recomendamos que inicies repentinamente, inicia poco a poco. Tambien te recomendamos hacer actividad física, tomar suficiente agua y dormir lo necesario.')
                        print('Si tu indice de masa corporal es bajo te recomendamos comer mas proteínas, comer mas calorias, incluir mas carbohidratos en tu vida, pero siempre teniendo cuidado de no comer alimentos altamente procesados') 
    
        IMC = calcula_imc(peso, altura)
        tabla.append(f'IMC: {IMC:.2f}')#el uso de :.2f para mandar solo dos decimales
        print(f'Tu IMC es {IMC:.2f}')
        
    elif opcion == 2:
        if tabla:
            print('Tabla de datos:')
            for i in tabla:
                print(i)
        else:
            print('No hay datos en la tabla.')

    elif opcion == 3:
        print('Saliendo del programa')
        break                           #para cerrar la función

    else:
        print('Opción no válida, por favor elige una opción del 1 al 3.')#si la opción no es valida

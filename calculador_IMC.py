#código de python


tabla = [] #para guardar los IMC calculados anteriormente 

while True:
    print('Bienvenido a tu calculadora de IMC\n')#menú interactivo
    print('El índice de masa corporal (IMC) es un método utiizado para estimar la cantidad de grasa corporal que tienen una persona, y determianr por tanto si el peso está dentro del rango normal, o po el contrario, si tiene sobreperso o delgadez. Con esta calculadora podras ver si tu IMC esta dentro de lo recomendado, y si no es así reciviras recomendaciones para llegar a tu IMC recomendado.\n') 
    print('Opción 1. Iniciar a calcular tu IMC\n')
    print('Opción 2. Accede a tu tabla de datos\n')
    print('Opción 3. Salir del programa\n')

    
    opcion = int(input('Selecciona tu opción: '))#seleccion de opciones

    if opcion == 1:
        def calcula_imc(peso, altura):#función en el que se hace el calculo del IMC
            imc = peso / (altura ** 2)
            return imc
        peso = float(input('Ingresa tu peso en kilogramos: \n'))
        altura = float(input('Ingresa tu altura en metros: \n'))
        dato3 = int(input('Ingresa tu edad: \n'))               #agregado para solicitar edad y dar consejeria

        IMC = calcula_imc(peso, altura)
        tabla.append(f'tus datos: Peso {peso}, altura: {altura}, tu edad: {dato3}, tu IMC: {IMC:.2f}')#el uso de :.2f para mandar solo dos decimales
        print(f'Tu IMC es {IMC:.2f}')
        if dato3 >= 65:
            if IMC >29:
                print('Tu IMC es mayor que lo recomendado\n')
                print('Tu indice de masa corporal ideal es entre 24-29, Tu indice de masa corporal es alto. Te recomendamos llevar una dieta balanceada, aunque no te recomendamos que inicies repentinamente, inicia poco a poco. Tambien te recomendamos hacer actividad física, tomar suficiente agua y dormir lo necesario.\n')
            elif IMC <24:
                print(' Tu indice de masa corporal ideal es entre 24-29. tu indice de masa corporal es bajo. Te recomendamos comer mas proteínas, comer mas calorias, incluir mas carbohidratos en tu vida, pero siempre teniendo cuidado de no comer alimentos altamente procesados\n')
            elif IMC >=24 or IMC <=29:
                print('Tu IMC es normal')   
        elif dato3 >= 55 and dato3 <= 64:
            if IMC >28:
                print('Tu IMC es mayor que lo recomendado\n')
                print('Tu indice de masa corporal ideal es entre 23-28, Tu indice de masa corporal es alto. Te recomendamos llevar una dieta balanceada, aunque no te recomendamos que inicies repentinamente, inicia poco a poco. Tambien te recomendamos hacer actividad física, tomar suficiente agua y dormir lo necesario.\n')
            elif IMC <23:
                print(' Tu indice de masa corporal ideal es entre 23-28. tu indice de masa corporal es bajo. Te recomendamos comer mas proteínas, comer mas calorias, incluir mas carbohidratos en tu vida, pero siempre teniendo cuidado de no comer alimentos altamente procesados\n')
            elif IMC >=23 or IMC <=28:
                print('Tu IMC es normal') 
        elif dato3 >= 45 and dato3 <= 54:
            if IMC >27:
                print('Tu IMC es mayor que lo recomendado\n')
                print('Tu indice de masa corporal ideal es entre 22-27, Tu indice de masa corporal es alto. Te recomendamos llevar una dieta balanceada, aunque no te recomendamos que inicies repentinamente, inicia poco a poco. Tambien te recomendamos hacer actividad física, tomar suficiente agua y dormir lo necesario.\n')
            elif IMC <22:
                print(' Tu indice de masa corporal ideal es entre 22-27. tu indice de masa corporal es bajo. Te recomendamos comer mas proteínas, comer mas calorias, incluir mas carbohidratos en tu vida, pero siempre teniendo cuidado de no comer alimentos altamente procesados\n')
            elif IMC >=22 or IMC <=27:
                print('Tu IMC es normal') 
        elif dato3 >= 35 and dato3 <= 44:
            if IMC >26:
                print('Tu IMC es mayor que lo recomendado\n')
                print('Tu indice de masa corporal ideal es entre 21-26, Tu indice de masa corporal es alto. Te recomendamos llevar una dieta balanceada, aunque no te recomendamos que inicies repentinamente, inicia poco a poco. Tambien te recomendamos hacer actividad física, tomar suficiente agua y dormir lo necesario.\n')
            elif IMC <21:
                print(' Tu indice de masa corporal ideal es entre 21-26. tu indice de masa corporal es bajo. Te recomendamos comer mas proteínas, comer mas calorias, incluir mas carbohidratos en tu vida, pero siempre teniendo cuidado de no comer alimentos altamente procesados\n')
            elif IMC >=21 or IMC <=26:
                print('Tu IMC es normal')
        elif dato3 >= 25 and dato3 <= 34:
            if IMC >25:
                print('Tu IMC es mayor que lo recomendado\n')
                print('Tu indice de masa corporal ideal es entre 20-25, Tu indice de masa corporal es alto. Te recomendamos llevar una dieta balanceada, aunque no te recomendamos que inicies repentinamente, inicia poco a poco. Tambien te recomendamos hacer actividad física, tomar suficiente agua y dormir lo necesario.\n')
            elif IMC <20:
                print(' Tu indice de masa corporal ideal es entre 20-25. tu indice de masa corporal es bajo. Te recomendamos comer mas proteínas, comer mas calorias, incluir mas carbohidratos en tu vida, pero siempre teniendo cuidado de no comer alimentos altamente procesados\n')
            elif IMC >=20 or IMC <=25:
                print('Tu IMC es normal') 
        elif dato3 >=18 and dato3 <= 24:
            if IMC >24:
                print('Tu IMC es mayor que lo recomendado\n')
                print('Tu indice de masa corporal ideal es entre 19-24, Tu indice de masa corporal es alto. Te recomendamos llevar una dieta balanceada, aunque no te recomendamos que inicies repentinamente, inicia poco a poco. Tambien te recomendamos hacer actividad física, tomar suficiente agua y dormir lo necesario.\n')
            elif IMC <19:
                print(' Tu indice de masa corporal ideal es entre 19-24. tu indice de masa corporal es bajo. Te recomendamos comer mas proteínas, comer mas calorias, incluir mas carbohidratos en tu vida, pero siempre teniendo cuidado de no comer alimentos altamente procesados\n')
            elif IMC >=19 or IMC <=24:
                print('Tu IMC es normal')  
        elif dato3 <18:
            if IMC >20:
                print('Tu IMC es mayor que lo recomendado\n')
                print('Tu indice de masa corporal ideal es entre 14-20, Tu indice de masa corporal es alto. Te recomendamos llevar una dieta balanceada, aunque no te recomendamos que inicies repentinamente, inicia poco a poco. Tambien te recomendamos hacer actividad física, tomar suficiente agua y dormir lo necesario.\n')
            elif IMC <14:
                print(' Tu indice de masa corporal ideal es entre 14-20. tu indice de masa corporal es bajo. Te recomendamos comer mas proteínas, comer mas calorias, incluir mas carbohidratos en tu vida, pero siempre teniendo cuidado de no comer alimentos altamente procesados\n')
            elif IMC >=14 or IMC <=20:
                print('Tu IMC es normal')
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

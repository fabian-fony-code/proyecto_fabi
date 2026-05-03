#edad = int(input("Escribe tu edad determinada: "))
# verificar o introducir un valor en la variable "edad"
#if edad >= 18:
    #print("¡Eres mayor de edad!")
    # if para verificar si edad es mayor o igual a 18, si es verdadera esa condicion, dara resultado 
    # el print de "Eres mayor de edad" en caso contrario, con else, verifica la condicion falsa y da un resultado, "Eres menor de edad"
#else:
    #print("¡Eres menor de edad!")

# estructura multiple

#temperatura = float(input("Ingrese la temperatura: "))

#if temperatura > 20:
    #print("Hace calor afuera...")
#elif temperatura >=15:
    #print("El clima es templado...")
    # elif extiende esta condicion y abre mas alla para distintos tipos mas de condiciones.
#else:
    #print ("Que frio hace afuera...")
    
# estructura anidada

#edad = int(input("Escribe tu edad!"))
#if edad < 0:
#    print("INVALIDO/ERROR, intentelo de nuevo.")
#else: 
#    if edad < 18:
#        print("Eres menor de edad.")
#    else:
#        if edad < 60:
#            print("Eres adulto.")
#        else:
#            print("Eres mayor de edad")

# estructura switch

#diff_num = int(input("Elija del 1 al 3, la dificultad del juego. (1. Facil, 2. Normal, 3. Dificil) "))
#if diff_num == 1:
        #print("Dificultad elegida: Facil. Buena suerte.")
#elif diff_num == 2:
        #print("Dificultad elegida: Normal. Buena suerte.")
#elif diff_num == 3:
        #print("Dificultad elegida: Dificil. Buena suerte, experto.")
#else:
        #print("Numero invalido, elija devuelta.")

# estructura con expresiones logicas

#entrada = True
#edad = 15
#es_invi = True
#black_list = False

#if (entrada and edad >= 18) or es_invi: #and para verificar que, segun la edad, la persona puede acceder a la pagina. or para que si es invitado y menor, igualmente pueda pasar por que es invitado.
#    if not black_list: #not es para que verifique de manera inversa la condicion, que en caso de ser falsa, diga que tiene el acceso denegado.
#        print("¡Acceso concedido! Bienvenido/a")
#    else:
#        print("Acceso denegado: Estás en la lista negra.")
#else:
#    print("Acceso denegado: No cumples los requisitos de entrada.")
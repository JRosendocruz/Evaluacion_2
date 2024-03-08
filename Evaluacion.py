import random
intentos=0

palabras=['carruaje','patines','carro','lancha','parangutirimicuaro','vaca','mono','pizza','laptop','teclas','uno','cien']

palabra = random.choice(palabras)
print(palabra)
totalLetas = len(palabra)

respuesta = ['-' for _ in range (len(palabra)) ]  # aqui se van almacenar las letras ingresadas
salida = ' '.join(respuesta)
print(salida)

print('Adivina la palabra con ', totalLetas, ' letras')
print("Adivina la palabra con", len(palabra), "letras")
print("-".join(respuesta))  # Mostrar la palabra inicialmente oculta
    
while intentos < 3 and '-' in respuesta:
        letra = input("Ingresa una letra: ").lower()
        
        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    respuesta[i] = letra
            print(" ".join(respuesta))
        else:
            intentos += 1
            print("Letra incorrecta. Te quedan", 3 - intentos, "intentos.")
    
            if '-' not in respuesta:
                  print("¡Felicidades! Has adivinado la palabra correctamente:", palabra)
            else:
                   print("¡Agotaste tus intentos! La palabra era:", palabra)

# Evaluación
'''
La evaluación se hace con un bucle while, donde el usuario ingresa una letra y
se evalua si esa letra está en la palabra a adivinar.
Si la letra está, se actualiza la respuesta con la letra.
Si no, se muestra un mensaje de error.
Sólo se tendrán 3 intentos, si se acierta la palabra o se agota los intentos,
el juego termina.
En lista llamada "respuesta" se debe almacer las letras que el usuario ingrese,
 reemplazando los guiones por las letras ingresadas


Ejemplo
Adivina la palabra con 8 letras
- - - - - - - -

Ingresa una letra: a
a - - - - - - - -
Ingresa una letra: e
a - - e - - - -

ALGORITMO

1. Realizar ciclo mientras el número de intentos sea menor a 3 o la palabra no esté completa
2.      Pedirle al usuario que ingrese una letra
3.      Verificar si la letra está en la palabra
4.      Si esta la letra, Actualizar la lista llamada respuesta
5.      Si no esta la letra, mostrar mensaje de error e incrementar el número de intentos
6.      Mostrar la lista llamada respuesta (que contiene las letras ingresadas y guiones)
7. Si la palabra está completa o se agotaron los intentos, terminar el ciclo

'''











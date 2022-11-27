from logging import exception


def es_primo(numero):
    contador = 0
#la idea es dividir el numero por todos los numero que estan entre 1 y el numero ingresado
    for i in range(1, numero + 1): # desde la divicion por 1 hasta el numero que ingreso el usuario
        if i == 1 or i == numero:  #validacmos si i es igual 1 o i es igual al numero ingresado, saltamos el ciclo
            continue
        if numero % i == 0:  # si el resultado de la division es cero aumentamos el contador
            contador += 1
    if contador == 0:
        return True
    else:
        return False
        

def run():  
    numero = int(input('Escribe un numero: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')

#para cada prueba se debe ejecutar el programa
if __name__ == '__main__':
    run()

#Constantes con los valores de los dados.
DADO_4=4
DADO_6=6
DADO_8=8
DADO_10=10
DADO_12=12
DADO_20=20

#Constante con el numero máximo de dados que se pueden tirar.
MAX_TIRADA=10

print("Bienvenido al simulador de dados")

#Creacion del menu principal.
while True:
   print("\nMenu principal")
   print("1. Tirar dados")
   print("2. Ver estadisticas")
   print("3. Salir")

#Controlamos los errores en caso de que el usuario no introduzca un numero.
   try:
    respuesta=int(input("Seleccione una opcion: "))
   except ValueError:
     print("Debes introducir un numero")
     continue
   
   match respuesta:

    case 1:

#Mostramos los tipos de dados que se pueden tirar y le pedimos al usuario que elija uno.
       print("Tipos de dados:")
       print("1. Dado de 4 caras")
       print("2. Dado de 6 caras")
       print("3. Dado de 8 caras")
       print("4. Dado de 10 caras")
       print("5. Dado de 12 caras")
       print("6. Dado de 20 caras")

       try:
        tipoDado=int(input("Selecciona el tipo de dado: "))
       except ValueError:
          print("Debes introducir un numero")
          continue
       
       match tipoDado:
        case 1:
           carasDado=DADO_4

        case 2:
           carasDado=DADO_6

        case 3:
           carasDado=DADO_8

        case 4:
           carasDado=DADO_10

        case 5:
           carasDado=DADO_12

        case 6:
           carasDado=DADO_20

        case _:
           print("El tipo de dado no es valido")
           continue
from rich.console import Console

#Constantes con los valores de los dados.
DADO_4= 4
DADO_6= 6
DADO_8= 8
DADO_10= 10
DADO_12= 12
DADO_20= 20

#Constante con el numero máximo de dados que se pueden tirar.
MAX_TIRADA= 10

#Creamos la consola de Rich 
console= Console()

console.print("[bold green]Bienvenido al simulador de dados[/bold green]")

#Creacion del menu principal.
while True:
   console.print("\n[bold cyan]Menu principal[/bold cyan]")
   console.print("1. Tirar dados")
   console.print("2. Ver estadisticas")
   console.print("3. Salir")

#Controlamos los errores en caso de que el usuario no introduzca un numero.
   try:
    respuesta= int(input("Seleccione una opcion: "))
   except ValueError:
     console.print("[red]Debes introducir un numero[/red]")
     continue
   
   match respuesta:

    case 1:

#Mostramos los tipos de dados que se pueden tirar y le pedimos al usuario que elija uno.
       console.print("Tipos de dados:")
       console.print("1. Dado de 4 caras")
       console.print("2. Dado de 6 caras")
       console.print("3. Dado de 8 caras")
       console.print("4. Dado de 10 caras")
       console.print("5. Dado de 12 caras")
       console.print("6. Dado de 20 caras")

       try:
        tipoDado= int(input("Selecciona el tipo de dado: "))
       except ValueError:
          console.print("[red]Debes introducir un numero[/red]")
          continue
       
       match tipoDado:
        case 1:
           carasDado= DADO_4

        case 2:
           carasDado= DADO_6

        case 3:
           carasDado= DADO_8

        case 4:
           carasDado= DADO_10

        case 5:
           carasDado= DADO_12

        case 6:
           carasDado= DADO_20

        case _:
           console.print("[red]El tipo de dado no es valido[/red]")
           continue

#Pedimos al usuario que introduzca el número de dados que quiere tirar.
       while True:

#Controlamos los errores en caso de que el usuario no introduzca un numero.
          try:
             cantidad= int(input(f"Introduce el numero de dados que quieres tirar (1-{MAX_TIRADA}): "))
          except ValueError:
             console.print("[red]Debes introducir un numero[/red]")
             continue

#Mediante este if controlamos que el numero de dados este entre 1 y el máximo de dados que hayamos puesto.
          if cantidad < 1 or cantidad > MAX_TIRADA:
             console.print(f"[red]El numero de dados debe estar entre 1 y {MAX_TIRADA}[/red]")
             continue
          else:
             break
          
    case 2:
       console.print("[yellow]Las estadisticas todavía no estan disponibles[/yellow]")
       pass
      
    case 3:
       console.print("[bold red]Saliendo del programa[/bold red]")
       break

    case _:
       console.print("[red]Opcion no valida[/red]")
       continue
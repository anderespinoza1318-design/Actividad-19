opcion = "0"

while opcion  !=  "3":
    print ("Hola Bienvenido ")
    print ("Este menú tiene 3 opciones y son las siguientes:")
    print ("1. Consultar su indice de masa corporal (IMC) ")
    print ("2. Operaciones Aritmeticas")
    print ("3. Salir")
    opcion = input("Digita la opcion aqui: ")

    if opcion == "1":
     print ("HOLA ")
     nombre = input ("Ingrese su Nombre: ")
     edad = input ("Ingrese su Edad: ")
     peso = float(input ("Ingrese su Peso (Kg): "))
     altura = float(input ("Ingrese su Altura (m): "))
     imc = peso / (altura ** 2)
     print ("Hola", nombre + " su Edad es de",  edad, "Años" " y su IMC es:", f"{imc:.2f}")
     volver = input ("Si deseas volver pulse 3,sino cualquier tecla: ")
     if volver != "3":
          opcion = "3"
          
     

    elif opcion == "2":
     print ("Hola, Aqui salen todas las Operaciones Aritmeticas")
     num1 = int(input (" Ingrese un primer numero: "))
     num2 = int(input ("Ingrese el segundo numero: ")) 
     suma = (num1+num2)
     resta = (num1-num2)
     multiplicación = (num1*num2)
     division = (num1/num2)
     divisionE = (num1//num2)
     potenciacion = ( num1**num2)
     print ("su suma es: ", suma) 
     print ("su resta es: ", resta)
     print ("su multiplicacion es: ", multiplicación)  
     print ("Su Division es: ", division)
     print ("Su Division Entera es: ", divisionE)
     print ("Su Potenciacion es: ", potenciacion)
     volver = input("Si deseas volver digite 3, sino cualquier tecla: ")
     if volver != "3":
          opcion = "3"
     
            
    elif opcion == "3":
     print("Saliendo, hasta luego")     
      
    else:
      print("Saliendo")
 
print ("Hola Bienvenido amigo")
print ("Este menú tiene 3 opciones y son las siguientes:")
print ("1. Consultar su indice de masa corporal (MIC) ")
print ("2. Operaciones Aritmeticas")
print ("3. Salir")
opcion = input("Digita la opcion aqui: ")

if opcion == "1":
     print ("HOLA ")
     nombre = input ("Ingrese su nombre: ")
     edad = input ("Ingrese su edad: ")
     peso = float(input ("Ingrese su peso: "))
     altura = float(input ("Ingrese su altura: "))
     alturacuadrado = (altura**2)
     print ("Bien ", nombre + " su Edad es ",  edad, "Años" " y su IMC es de ",  (peso/alturacuadrado))
     salir1 = input ("Si deseas volver pulse 3: ")
     while salir1 == "3":
          print ("1. Consultar su indice de masa corporal (MIC) ")
          print ("2. Operaciones Aritmeticas")
          print ("3. Salir") 
          opcion = input("Digita la opcion aqui: ")
          break

elif opcion == "2":
     print ("Aqui salen todas las Operaciones Aritmeticas")
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
     salir2 = input("Si deseas volver digite 3: ")
     while salir2 == "3":
            print ("1. Consultar su indice de masa corporal (MIC) ")
            print ("2. Operaciones Aritmeticas")
            print ("3. Salir") 
            opcion = input("Digita la opcion aqui: ")
            break
          

else:
      print("Saliendo")


     
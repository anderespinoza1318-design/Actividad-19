print("Hola")

opcion = "0"

while opcion != "3":
    print("\nzBienvenido al menu principal")
    print("1. Consultar su indice de masa corporal (IMC)")
    print("2. Operaciones Aritmeticas")
    print("3. Salir")
    opcion = input("Digita la opcion aqui: ")

    if opcion == "1":
        nombre = input("Ingrese su nombre: ")
        edad = input("Ingrese su edad: ")
        peso = float(input("Ingrese su peso (kg): "))
        altura = float(input("Ingrese su altura (m): "))
        alturacuadrado = altura ** 2
        imc = peso / alturacuadrado
        print("Bien", nombre, "su edad es de", edad, "anos y su IMC es de", imc)
        volver = input("Deseas volver al menu? Pulsa 3, sino pulsa cualquier tecla: ")
        if volver != "3":
            opcion = "3"

    elif opcion == "2":
        print("Aqui salen todas las Operaciones Aritmeticas")
        num1 = int(input("Ingrese un primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2
        divisionE = num1 // num2
        potenciacion = num1 ** num2
        print("Su suma es:", suma)
        print("Su resta es:", resta)
        print("Su multiplicacion es:", multiplicacion)
        print("Su division es:", division)
        print("Su division entera es:", divisionE)
        print("Su potenciacion es:", potenciacion)
        volver = input("Deseas volver al menu? Pulsa 3, sino pulsa cualquier tecla: ")
        if volver != "3":
            opcion = "3"

    elif opcion == "3":
        print("Saliendo... Gracias por usar!")

    else:
        print("Opcion no valida. Elige 1, 2 o 3.")
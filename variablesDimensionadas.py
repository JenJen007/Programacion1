from funciones import *


while True:
    print("Menú:")
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Consultar destino por DNI")
    print("4. Consultar cantidad de pasajeros por ciudad")
    print("5. Consultar país por DNI")
    print("6. Consultar cantidad de pasajeros por país")
    print("7. Salir")

    option = input("Selecciona una opción: ")

    if option == '1':
        name = input("Nombre del pasajero: ")
        dni = int(input("DNI del pasajero: "))
        destiny = input("Destino del pasajero: ")
        add_passangers(list_passangers, name, dni, destiny)
    elif option == '2':
        city = input("Nombre de la ciudad: ")
        country = input("Nombre del país: ")
        add_city(list_cities, city, country)
    elif option == '3':
        dni = int(input("DNI del pasajero: "))
        destiny = obtain_city_for_dni(list_passangers, dni)
        if destiny:
            print(f"El pasajero con DNI {dni} viaja a {destiny}.")
        else:
            print("No se encontró un pasajero con ese DNI.")
    elif option == '4':
        city = input("Nombre de la ciudad: ")
        cant_passangers = obtain_cant_of_passangers_for_city(list_passangers, city)
        print(f"La cantidad de pasajeros que viajan a {city} es: {cant_passangers}")
    elif option == '5':
        dni = int(input("DNI del pasajero: "))
        destiny = obtain_city_for_dni(list_passangers, dni)
        if destiny:
            country = obtain_country_for_city(list_cities, destiny)
            print(f"El pasajero con DNI {dni} viaja a {country}.")
        else:
            print("No se encontró un pasajero con ese DNI.")
    elif option == '6':
        country = input("Nombre del país: ")
        cant_passangers = obtain_cant_passangers_for_country(list_passangers, country)
        print(f"La cantidad de pasajeros que viajan a {country} es: {cant_passangers}")
    elif option == '7':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

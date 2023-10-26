#funcion para sumar digitos
def sumatoria(x):
    add = 0
    while x != 0:
        digit = x%10
        x //= 10
        add += digit
    return add

#Funciones para ejercicio de variables dimensionadas
list_passangers = []
list_cities = []
def add_passangers(list_passangers, name, dni, destiny):
    list_passangers.append((name, dni, destiny))

def add_city(list_cities, city, country):
    list_cities.append((city, country))

def obtain_city_for_dni(list_passangers, dni):
    for name, dni_passanger, destiny in list_passangers:
        if dni_passanger == dni:
            return destiny
    return None

def obtain_cant_of_passangers_for_city(list_passangers, city):
    count = 0
    for name, dni, destiny in list_passangers:
        if destiny == city:
            count += 1
    return count

def obtain_country_for_city(list_cities, city):
    for name_city, country in list_cities:
        if name_city == city:
            return country
    return None

def obtain_cant_passangers_for_country(list_passangers, country):
    count = 0
    for name, dni, destiny in list_passangers:
        if obtain_country_for_city(list_cities, destiny) == country:
            count += 1
    return count


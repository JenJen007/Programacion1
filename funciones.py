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

#Funciones para ordenamiento y búsqueda
# Función para Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Función para Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Función para Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Función para Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Función para Búsqueda Lineal
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

# Función para Búsqueda Binaria (Requiere una lista ordenada)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

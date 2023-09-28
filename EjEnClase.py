#Pido al usuario que ingrese el dia de la semana y lo guarda en variable date
date = input("Ingrese el día de la semana en formato día, DD/MM: ").lower()
#
day_week = str(date[0:date.find(',')])
day = int(date[date.find(' ') + 1:date.find('/')])
month = int(date[date.find('/') + 1:])
#Creamos una lista y guardamos los días de la semana
my_list = ["Lunes", "Martes","Miércoles","Jueves","Viernes"]
print(date)
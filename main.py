def hello_world(word):
	return word

print(hello_world(word="Holi uwu"))

import datetime

nombre = input("¿Cómo te llamas? ")
hoy = datetime.datetime.now()
dia_de_la_semana = hoy.strftime("%A")

print("Hola " + nombre + ", ¡hoy es " + dia_de_la_semana + ", así que eres un " + dia_de_la_semana.lower() + "!")


#Te dej o un program que te dice que dia de la semana es utilizando tu nombre
#ARG

from asyncore import close_all
import random
while True:
    try:
        archivo = open(input("Ingrese el nombre de su archivo. ").strip())
    except FileNotFoundError: 
        print("El archivo actual es inexistente.")
    else:
        break

lineas = archivo.readlines()

texto = "".join(lineas)

palabras = texto.split()

caracteres = len(texto)

palabras_en_numero = len(palabras)

promedio = caracteres / palabras_en_numero

palabras_lista = []

for palabra in palabras:
   palabras_lista.append((len(palabra),palabra))

palabras_ordenadas = sorted(palabras_lista)



#print(promedio)
print ("La longitud promedio de letras es de ""{0:.2f}".format(promedio), "letras ") 


print("El archivo contiene", palabras_en_numero, "palabras.")


print("\nLa palabra mas larga del texto es", "", palabras_ordenadas[-1][1], " y tiene", len(palabras_ordenadas[-1][1]), "letras")


solicitar_cantidad_de_letras = int(input("Introduzca la cantidad de letras:  "))

if solicitar_cantidad_de_letras == 0:
    close_all

else:

    palabras_que_coinciden = []
    for palabrita in palabras:
        if solicitar_cantidad_de_letras == len(palabrita):
            palabras_que_coinciden.append(palabrita)

    if len(palabras_que_coinciden) < 20:
        print(*palabras_que_coinciden)

    else:
    
        seleccion_aleatoria = random.sample(palabras_que_coinciden, 20)

        print('  '.join(seleccion_aleatoria))
        
        
        
        
        
    


    

        









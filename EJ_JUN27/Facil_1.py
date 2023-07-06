"""1) primer reto facil, pasar de un numero romano como xx == 20, de letras a enteros.
"""

def f(z): # z sera el numero que estara en romano
    # primero pongamos los valores de todas las letras
    letras = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000, "0" : 0}
    
    z = z + "0" # esto para despues cuando vayamos a recorrer todo con tranquilidad

    sum = 0 
    for i in range(len(z[:-1])):
        # vamos a hacer filtro para cada numero que se resta
        if z[i] == "I" and (z[i + 1]) == "V": 
            sum += 4
            z = z.replace(z[i+1],"0") # esto lo hice para que no se sumara de nuevo el siguiente valor, entonces lo reemplzo por un cero 
        elif z[i] == "I" and (z[i + 1]) == "X":
            sum += 9
            z = z.replace(z[i+1],"0")
        elif z[i] == "X" and (z[i + 1]) == "L":
            sum += 40
            z = z.replace(z[i+1],"0")
        elif z[i] == "X" and (z[i + 1]) == "C":
            sum += 90
            z = z.replace(z[i+1],"0")
        elif z[i] == "C" and (z[i + 1]) == "D":
            sum += 400
            z = z.replace(z[i+1],"0")
        elif z[i] == "C" and (z[i + 1]) == "M":
            sum += 900
            z = z.replace(z[i+1],"0")
        else:
            sum += letras[z[i]]
    return sum

z = "MMI"
print(f(z))

# ESO ES TODO PA 










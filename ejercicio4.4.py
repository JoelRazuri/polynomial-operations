"""
    Escribir funciones que permitan encontrar:
        a) El máximo o mínimo de un polinomio de segundo grado (dados los coeficientes a, b y
        c, indicando si es un máximo o un mínimo.
        b) Las raíces (reales o complejas) de un polinomio de segundo grado.
        Nota: validar que las operaciones puedan efectuarse antes de realizarlas (no dividir por
        cero, ni calcular la raíz de un número negativo).
        c) La intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta).
        Nota: validar que no sean dos rectas con la misma pendiente, antes de efectuar la operación.
"""
import math

def max_min_polinomio(a,b,c):
    # Indica el máximo o mínimo de un polinomio de segundo grado según los coeficientes a, b y c.

    xv=-b/(2*a)
    yv=a*xv**2 + b*xv + c
    
    print("")

    if a<0:
        print(f"La función {a}x^2 + {b}x + {c} tiene un mínimo en el punto ({xv},{yv}).")
    else:
        print(f"La función {a}x^2 + {b}x + {c} tiene un máximo en el punto ({xv},{yv}).")


# max_min_polinomio(2,5,3)
# max_min_polinomio(-2,-1,9)
# max_min_polinomio(3,4,6)
# max_min_polinomio(-8,-3,5)

print("")

def raices_polinomio(a,b,c):
    # Indica las raíces (reales o complejas) de un polinomio de segundo grado.

    discriminante=b**2-(4*a*c)

    if a==0:
        print("No tiene raiz, el coeficiente 'a' tiene que ser distinto de cero.")
    else:
        if (discriminante>=0):
            x1= (-b + math.sqrt(discriminante)) / 2*a
            x2= (-b - math.sqrt(discriminante)) / 2*a
            print(f"La función {a}x^2 + {b}x + {c}, tiene raíces x1= {x1} y x2= {x2}")
        else:
            discriminante= -1 * discriminante
            xreal=-b/2*a
            ximaginario=math.sqrt(discriminante)/2*a
            print(f"La función {a}x^2 + {b}x + {c}, tiene raíces x1= {xreal} + {ximaginario} i y x2= {xreal} - {ximaginario} i")
                 

raices_polinomio(1,-10,34)


def intersección_rectas(pendiente1,ordenada1,pendiente2,ordenada2):
    # Indica la intersección de dos rectas dadas sus pendientes y oerdenadas al origen.

    if (pendiente1==pendiente2):
        print("No hay intersección porque las rectas son paralelas.")
    else:
        x= (ordenada2 - ordenada1) / (pendiente1 - pendiente2)
        y= pendiente1*x + ordenada1
        print(f"Las dos rectas tiene intersección en el punto ({x},{y}).")


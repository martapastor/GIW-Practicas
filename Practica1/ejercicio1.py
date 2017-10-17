
# coding: utf-8

# Víctor Fernández Rubio
# David González Jiménez
# Carlos Llames Arribas
# Marta Pastor Puente

# We will calculate how many bills we have to return
def billete(x, vuelta):
    # We only print the change if we return at least one bill of the given value
    if (vuelta // x > 0.0):
        print ("Billete", x, ":", vuelta // x)
    return (vuelta % x)



# We will calculate how many coins we have to return
def monedas(y, vuelta):
    # We only print the change if we return at least one coin of the given value
    if (vuelta // y > 0.0):
        print ("Moneda", y, ":", vuelta // y)
    return (vuelta % y)


# We will calculate how many coins and bills and of which value we have to given
# in return to obtain the most efficient change strategy
def cambio (precio, dinero):
    print ("\nVueltas:")

    # We save the different values of bills and coins (in €) in two arrays to
    # traverse later
    billetes = [500, 200, 100, 50, 20, 10, 5]
    moneda = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
    vueltas = dinero - precio

    # We will use two counters to store the index of the element of the array we
    # have to access
    i = 0
    j = 0

    # While we still have change to return...
    while(vueltas >= 0.01):
        # ... and it is greater than five so we can use bills...
        while(vueltas >= 5):
            # We calculate how many bills we have to give in return
            vueltas = billete(billetes[i], vueltas)
            i += 1
        # We calculate how many coins we have to give in return
        vueltas = monedas(moneda[j], vueltas)
        j += 1



if __name__ == "__main__":
    PVP = input ("¿Cuánto cuesta?\n")
    midinero = input ("¿Cuánto dinero tengo?\n")

    cambio(float(PVP), float(midinero))

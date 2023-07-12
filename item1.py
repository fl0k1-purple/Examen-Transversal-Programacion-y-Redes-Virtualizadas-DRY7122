from random import shuffle

integrantes = ["Andrés Tapia Olguín", "Martín Muñoz Toro", "Benjamín Peña Medrano"]

shuffle(integrantes)

for i in range(len(integrantes)):
    print("{}. {}".format(i+1, integrantes[i]))
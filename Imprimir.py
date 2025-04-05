#Convinar textos y numeros
#Forma 1:
a = "Carlos"
b = 20
print("Hola ",a," tienes ",b)
#Forma 2:
c = "Hola " + str(a) + " tienes " + str(b)
print(c)
#Forma 3:
d = f"Hola {a} tienes {b + 10}"
print(d)
#Separadores en imprimir
print("Carlos", "Jose", "Juan") #(Normal)
print("Carlos", "Jose", "Juan", sep ="*")
print("Carlos", "Jose", "Juan", sep ="*", end = "%\n")

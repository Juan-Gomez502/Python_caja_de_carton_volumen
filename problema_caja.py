print("valores:")

largo=float(input("ingrese el largo de su carton:"))
ancho=float(input("ingrese el ancho de su carton:")) 
h=1
v=((ancho-2*h)*(largo*2*h)*h)
vmax=0 
while vmax<v:
    vmax=v
    h=h+1
    v=((ancho-2*h)*(largo*2*h)*h)

print("altura que maximiza el volumen:", h)
print("el volumen maximo es de:",v)
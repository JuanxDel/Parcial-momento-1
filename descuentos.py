m=float(input("Ingrese el monto de la compra:"))
if m<50:
    d=0
    v=m 
elif m>=50 and m<=100:
    d=m*0.05
    v=m-d
elif m>100:
    d=m*0.1
    v=m-d
print("Descuento Aplicado:",d)
print("Total a pagar:",v)
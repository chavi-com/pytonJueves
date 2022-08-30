'''
numero=5

while(numero<10):
    print("estoy adentro de la cuerda")
    print("DOS")
    numero=numero+1
else:
    print("adios")    

print("estoy por fuera de la cuerda")

'''
opcion=1
print("******menu******")
print("1.sumar")
print("2.restar")
print("o.salir")

while(opcion !=0):
    opcion=int(input("dijite una opcion: "))
    if(opcion==1):
        print("sumando")
    elif(opcion==2):
        print("restando") 
    elif(opcion==0):
        print("finalizado")
        break 

    else:
        print("dijita una opcion valida")    
'''contador=0
suma=0


while (contador >=0):
    contador=int(input("dijita un entero"))
    if(contador>=0):
        suma=suma+contador
    
    else:
        print("fin")
        print(f'la suma fue: {suma}')
        break


else:    
    print  (f'la suma fue: {suma}')  '''

#multiplo de 3

numero = int(input("dijita un numero entero : "))
modulo = numero % 3
print(f'el modulo del numero es: {modulo}')

if modulo == 0:
    print(f'el numero{numero} es multiplo de 3')

else:
    print(f'el numero {numero} no es multiplo')    
print("fin")








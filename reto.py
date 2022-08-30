contador=0
suma=0


while (contador >=0):
    contador=int(input("dijita un entero"))
    if(contador>=0):
        suma=suma+contador
    
    else:
        print("fin")
        #print(f'la suma fue: {suma}')
        break

else:    
    print(f'la suma fue: {suma}')    



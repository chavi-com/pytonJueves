#definir variable de control

contador=0

#contador de numeros negativos

contN=0

while(contador<5):
    numero=int(input("ingrese un numero"))
    if(numero<0):
        contN=contN+1
    else:
        contN=contN

print(f'la suma de negativos es {contN}')        
      
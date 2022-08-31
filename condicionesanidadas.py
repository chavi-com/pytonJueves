'''condiciones anidadas elif'''
sensorNivelAgua=int(input("Digite el nivel de agua actual"))

if(sensorNivelAgua>=0 and sensorNivelAgua <20):
    print(f"peligro el nivel{sensorNivelAgua} es peligroso")

elif(sensorNivelAgua>=20 and sensorNivelAgua<400):  
    print(f"el nivel de agua es normal{sensorNivelAgua}")  
elif(sensorNivelAgua >=400):
    print(f"peligro el nivel{sensorNivelAgua} es peligroso")
else:
    print(f"peligro el nivel no es valido")   
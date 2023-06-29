import datetime
#the variable "tiempo" is for store hour, day , etc.
tiempo = datetime.datetime.now()
print("la hora es :  ", "\n" , tiempo.hour,":",  tiempo.minute)
# I make a cicle "if" for define the functionalty of the program  
if tiempo.hour > 18 and tiempo.minute > 1:
    print("es hora de descannsar")
else:
    hora = 19 - tiempo.hour
    minuto = 60 - tiempo.minute 
    print("un te falta trabajar","\n",hora,":", minuto  )

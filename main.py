#import moduloA
import paquete2.moduloB

#from paquete2 import moduloB


print ("Hola mundo")

print(f"__name__: {__name__}")

#a=moduloA.A()
#print(a.saludo())

b=paquete2.moduloB.B()
print(b.captura_mensaje())

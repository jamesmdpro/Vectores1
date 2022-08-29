#Definir los vectores

A = []
B = []
C = []  #suma
D = []  #resta
E = []  # multiplicacion
N = int(input('Cuantas dimenciones necesita calcular : '))

for f in range (0,N ,1):
    x = int(input('Digite un Elemento de A: '))
    A.append( x )
for f in range (0,N ,1):
    x = int(input('Digite un Elemento de B: '))
    B.append( x )
for f in range (0,N ,1):
    C.append(A[f] + B[f])
for f in range (0,N ,1):
    D.append(A[f] - B[f])
for f in range (0,N ,1):
    E.append(A[f] * B[f])

print('Lista A: ', A)
print('Lista B: ', B)
print('Suma : ', C)
print('Resta : ', D)
print('Multiplicacion : ', E)
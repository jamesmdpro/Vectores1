
class datosVectores:
    def __init__(self, A , B , C, N):
        self.A = A
        self.B = B
        self.C = C
        self.N = N

    A = []
    B = []
    C = []
    N = int(input('Cuantos vectores necesita calcular : '))

for f in range (0,datosVectores.N ,1):
    x = int(input('Digite un Elemento de A: '))
    datosVectores.A.append(x)
for f in range (0,datosVectores.N ,1):
    x = int(input('Digite un Elemento de B: '))
    datosVectores.B.append(x)

for f in range (0,datosVectores.N ,1):
    datosVectores.C.append(datosVectores.A[f] + datosVectores.B[f])


print('Suma de vectores'.center(50, '-'))


print('Lista A: ', datosVectores.A)
print('Lista B: ', datosVectores.B)
print('Suma : ', datosVectores.C)
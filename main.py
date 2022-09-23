import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
def acc_mat_vec1(mat,vec):
    """
    matriz,vector->matriz/vector
    retorna el resultado de el producto de un vector y una matriz
    """
    fil=len(mat)
    new_vec=[0 for i in range(fil)]
    for i in range(len(mat)):
        valor=(0,0)
        for j in range(len(mat[i])):
            valor=suma(valor,producto(mat[i][j],vec[j]))
        new_vec[i]=valor
    return new_vec
def acc_mat_vec(mat, vec):
    """
    matriz,vector->matriz/vector
    retorna el resultado de el producto de un vector y una matriz
    """
    fil = len(mat)
    new_vec = [0 for i in range(fil)]
    for i in range(len(mat)):
        valor = 0
        for j in range(len(mat[i])):
            valor +=mat[i][j]*vec[j]
        new_vec[i] = valor
    return new_vec
def traspuesta(mat):
    """
    mat->mat
    retorna la traspuesta de una matriz
    """
    if type(mat[0])==int:
        new_mat = [[] for i in range(len(mat))]
        for i in range(len(mat)):
            new_mat[i].append(mat[i])
    else:
        new_mat = [[] for i in range(len(mat[0]))]
        for i in range(len(mat[0])):
            for j in range(len(mat)):
                new_mat[i].append(mat[j][i])
    return new_mat
def suma(num1,num2):
    """Tupla,Tupla->Tupla
    Retorna la suma de dos numeros complejos
    """
    return (num1[0]+num2[0],num1[1]+num2[1])
def producto(num1,num2):
    """Tupla,Tupla->Tupla
    Retorna el producto de dos numeros complejos
    """
    return ( round(num1[0]*num2[0]-num1[1]*num2[1],2),round(num1[0]*num2[1]+num1[1]*num2[0],2))
def exp_mult_rend(mat,vec,click):
    new_mat=traspuesta(mat[:])
    for i in new_mat:
        if sum(i)!=0:
            return False
    for _ in range(click):
        vec=acc_mat_vec(mat,vec)
    return vec
def exp_canicas(mat,vec,clicks):
    for _ in range(clicks):
        vec=acc_mat_vec(mat,vec)
    return vec
def exp_can_cuant(mat,vec,clicks):
    for i in range(clicks):
        vec=acc_mat_vec1(mat,vec)
    return vec
# Plot a histogram
counts = {'1':0.25, '2':0.2, '3':0.2,
        '4':.35}
plot_histogram(counts)
plt.show()
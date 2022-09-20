def exp_canicas(mat,vec):
    print('Ingrese x si quiere realizar un "click" o "N" si quiere finalizar ')
    ins=input()
    while ins=="x":
        vec=acc_mat_vec(mat,vec)
        for i in vec:
            print(i)
        ins = input()
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


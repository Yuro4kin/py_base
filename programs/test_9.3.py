

# 3. Написать программу сложения двух матриц
#       [ 1  2 ]    [ 1  0 ]
#  C = A[ 3  4 ] + B[ 0  1 ]
#       [ 5  6 ]    [ 1  1 ]
#
#
# Двумерные списки - неквадратная матрица A и B состоящая из элементов размером 3 х 2
AA = [[1,2], [3,4], [5,6]]
BB = [[1,0], [0,1], [1,1]]
# Обратимся к конкретному числу в матрице
           
C = [[AA[0][0]+BB[0][0]]+[AA[0][1]+BB[0][1]]] + [[AA[1][0]+BB[1][0]]+[AA[1][1]+BB[1][1]]]  +  [[AA[2][0]+BB[2][0]]+[AA[2][1]+BB[2][1]]] 
print("Неквадратная матрица A размером 3 х 2: ", AA)
print("Неквадратная матрица B размером 3 х 2: ", BB)
print("Выполнено сложение двух матриц: ", C) 


A = [[1,2],[3,4],[5,6]]
B = [[1,0],[0,1],[1,1]]

X = [[0,0],[0,0],[0,0]]

for i in range(len(A)):
    for j in range(len(X[0])):
        X[i][j] = A[i][j] + B[i][j]

print(X) 
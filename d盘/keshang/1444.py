# def movedisk(i, x,y):
#     print('直接将',i,'从', x,'移到', y)
#
# def move(n,a,b,c):
#     if n ==1:
#         movedisk(n,a,c)
#         return
#     move(n-1, a,c, b)
#     movedisk(n,a,c)
#     move(n-1, b, a,c)
#
#
#
#
#
# move(5,'a', 'b', 'c')

#
# l = [[1,2,3],
#      [4,5,6],
#      [7,8,9]
#      ]
# for i in reversed(range(len(l))):
#     for j in range(len(l[i])):
#         l[j][i-2]=l[i][j]
#
# for k in l:
#     print(l)




from copy import deepcopy


matrix1 = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

len_m = len(matrix1)
matrix3 = [0 for i in range(len_m)]
print(matrix3)

matrix2 = [[0 for j in range(len_m)] for i in range(len_m)]
print(matrix2)

# for a in range(len_m):
#     for b in range(len_m):
#         matrix2[b][len_m-1-a] = matrix1[a][b]
#
# for k in matrix2:
#     print(k)


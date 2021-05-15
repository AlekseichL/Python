#Сложение матриц 3 на 2
class Matrix:
    def __init__(self, l1):
        self.l1=l1

    def __str__(self):
        return f"Матрица: \n{self.l1[0]} \n{self.l1[1]} \n{self.l1[2]}"

    def __add__(self, other):
        matr = [[0, 0],
                [0, 0],
                [0, 0]]

        for i in range(len(self.l1)):
            for j in range(len(self.l1[i])):
                matr[i][j] = self.l1[i][j] + other.l1[i][j]

        return f"Результат сложения матриц: \n{matr[0]}\n{matr[1]},\n{matr[2]}"

mat1=Matrix([[2, 4], [5, 8], [8, 9]])
print(mat1)
print(' ')
mat2=Matrix([[3, 8], [9, 4], [2, 6]])
print(mat2)
print(' ')
print(mat1+mat2)

# class Matrix:
#     def __init__(self, l1, l2):
#         self.l1=l1
#         self.l2=l2
#
#
#     def __str__(self):
#         return f"Матрица №1: \n{self.l1[0]}\n{self.l1[1]}\n{self.l1[2]}\
#         \n\nМатрица №2: \n{self.l2[0]}\n{self.l2[1]}\n{self.l2[2]} "
#
#     def __add__(self):
#         matr = [[0, 0],
#                 [0, 0],
#                 [0, 0]]
#
#         for i in range(len(self.l1)):
#             for j in range(len(self.l2[i])):
#                 matr[i][j] = self.l1[i][j] + self.l2[i][j]
#
#         return f"Результат сложения матриц: \n{matr[0]}\n{matr[1]},\n{matr[2]}"
#
# mat=Matrix([[2, 4], [5, 8], [8, 9]],[[3, 8], [9, 4], [2, 6]])
# print(mat)
# print(' ')
# print(mat.__add__())


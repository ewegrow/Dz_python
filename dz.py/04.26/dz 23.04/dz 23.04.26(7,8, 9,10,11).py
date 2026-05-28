import random

def matrix(m, n):
    return [[random.randint(1, 100) for _ in range(n)] for _ in range(m)]

def find(matrix):
    min_val = max_val = matrix[0][0]
    min_idx = max_idx = (0,0)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            current = matrix[i][j]
            if current < min_val:
                min_val = current
                min_idx = (i,j)
            if current > max_val:
                max_val = current
                max_idx = (i,j)
    return min_idx, max_idx

def analyze_sums(matrix):
    total_sum = sum(sum(row) for row in matrix)
    print(f"\nОбщая сумма всех элементов: {total_sum}")
    if total_sum == 0: return 
    num_cols = len(matrix[0])
    for j in range(num_cols):
        column_sum = sum(row[j] for row in matrix)
        percentage = (column_sum / total_sum) * 100
        print(f"Столбец {j}: сумма = {column_sum}, доля = {percentage:.2f}%")


def multiply_by_col_k(matrix, k):
    new_matrix = [row[:] for row in matrix]
    for i in range(len(matrix)):
        multiplier = matrix[i][k]
        for j in range(len(matrix[0])):
            new_matrix[i][j] *= multiplier
    return new_matrix


def sum_with_row_l(matrix, l):
    new_matrix = [row[:] for row in matrix]
    target_row = matrix[l]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[i][j] += target_row[j]
    return new_matrix


rows = int(input("Введите количество строк (м): "))
cols = int(input("Введите количество столбцов (n): "))

cr_matrix = matrix(rows, cols)

print(f"\nМатрица {rows} x {cols}:")
for row in cr_matrix:
    print(row)

min_c, max_c = find(cr_matrix)
print(f"\nМинимальный индекс: {min_c}")
print(f"Максимальный индекс: {max_c}")

analyze_sums(cr_matrix)

k = int(input(f"\nВведите индекс столбца K для умножения (0-{cols-1}): "))
res_k = multiply_by_col_k(cr_matrix, k)
print(f"Матрица после умножения на столбец {k}:")
for row in res_k: print(row)

l = int(input(f"\nВведите индекс строки L для сложения (0-{rows-1}): "))
res_l = sum_with_row_l(cr_matrix, l)
print(f"Матрица после сложения со строкой {l}:")
for row in res_l: print(row)

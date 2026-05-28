def main():
    
    try:
        m = int(input("Введите количество строк (M): "))
        n = int(input("Введите количество столбцов (N): "))
        
        matrix = []
        print(f"Введите элементы матрицы по строкам (через пробел, только 0 и 1 для корректности 3-й задачи):")
        for i in range(m):
            row = list(map(float, input(f"Строка {i+1}: ").split()))
            if len(row) != n:
                print(f"Ошибка: должно быть ровно {n} элементов. Попробуйте снова.")
                return
            matrix.append(row)
            
        h = float(input("\nВведите число H для поиска в столбцах: "))
    except ValueError:
        print("Ошибка: вводите только числа.")
        return

    
    def task_find_h(mat, val):
        with_h = []
        without_h = []
        rows_cnt = len(mat)
        cols_cnt = len(mat[0])
        
        for j in range(cols_cnt):
            
            column = [mat[i][j] for i in range(rows_cnt)]
            if val in column:
                with_h.append(j)
            else:
                without_h.append(j)
        return with_h, without_h

    
    def task_diagonals(mat):
        m_sum = 0
        s_sum = 0
        rows_cnt = len(mat)
        cols_cnt = len(mat[0])
        
        size = min(rows_cnt, cols_cnt)
        
        for i in range(size):
            m_sum += mat[i][i]
            s_sum += mat[i][cols_cnt - 1 - i]
        return m_sum, s_sum

    
    def task_parity(mat):
        new_mat = [row[:] for row in mat]
        for row in new_mat:
            ones = row.count(1.0)
            row.append(1.0 if ones % 2 != 0 else 0.0)
        return new_mat

    
    print("\n" + "="*30)
    
    wh, woh = task_find_h(matrix, h)
    print(f"1. Столбцы с числом {h}: {wh}")
    print(f"   Столбцы без числа {h}: {woh}")

    ms, ss = task_diagonals(matrix)
    print(f"2. Сумма главной диагонали: {ms}")
    print(f"   Сумма побочной диагонали: {ss}")

    res_matrix = task_parity(matrix)
    print("3. Матрица с добавленным столбцом четности:")
    for r in res_matrix:
        print([int(x) if x.is_integer() else x for x in r]) 

if __name__ == "__main__":
    main()

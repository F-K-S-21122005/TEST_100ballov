def is_safe(board, x, y):
    # Проверяем, не находится ли клетка под боем.
    for i in range(8):
        if board[x][i] == 1 or board[i][y] == 1:  # Ладья бьет по вертикали или горизонтали
            return False
    return True

def place_rooks(board, rooks, m, solutions):
    if len(rooks) == m:
        # Если поставили M фигур, сохраняем решение
        solutions.append(rooks[:])
        return
    
    for i in range(8):
        for j in range(8):
            if is_safe(board, i, j):
                board[i][j] = 1
                rooks.append((i, j))
                place_rooks(board, rooks, m, solutions)
                rooks.pop()
                board[i][j] = 0

def find_solutions(n, m, initial_rooks):
    board = [[0] * 8 for _ in range(8)]  # Инициализация пустой доски
    
    # Размещаем уже существующие ладьи
    for x, y in initial_rooks:
        board[x][y] = 1

    solutions = []
    place_rooks(board, [], m, solutions)
    
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        print(" ".join(f"({x},{y})" for x, y in solution))

# Ввод данных
n, m = map(int, input().split())
initial_rooks = [tuple(map(int, input().split())) for _ in range(n)]

# Находим все решения
solutions = find_solutions(n, m, initial_rooks)

# Выводим все решения
print_solutions(solutions)
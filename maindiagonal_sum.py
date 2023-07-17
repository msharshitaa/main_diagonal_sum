def main_diagonal_sum(matrix, row, col):
    sum = 0
    for i in range(row):
        for j in range(col):
            if i == j:
                sum += matrix[i][j]
    return sum
row=int(input())
col=int(input())
matrix = []
for i in range(row):
    matrix.append(list(map(int, input().split())))
print(main_diagonal_sum(matrix, row, col))

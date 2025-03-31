def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)
        triangle.append(row)

    max_width = len("   ".join(map(str, triangle[-1])))  # Son satırın genişliği
    for row in triangle:
        row_str = "   ".join(map(str, row))
        print(row_str.center(max_width))



n = 5
generate_pascals_triangle(n)


lines = int(input())
rows = int(input())
 
array = []
 
for i in range(int(lines)):
    array.append(list(map(int, input().split())))
 
coordinate_line = int(input())
coordinate_row = int(input())
 
 
def get_neighbours(coordinate_line, coordinate_row):
    results = []
 
    if lines <= 1 and rows <= 1:
        return results
 
    # не выходит здесь из функции
    if coordinate_line < 0 or coordinate_row < 0:
        return results
 
    if lines == 1:
        pass
    elif coordinate_line == 0:
        results.append(array[coordinate_line + 1][coordinate_row])
    elif coordinate_line == lines - 1:
        results.append(array[coordinate_line - 1][coordinate_row])
    else:
        results.append(array[coordinate_line + 1][coordinate_row])
        results.append(array[coordinate_line - 1][coordinate_row])

    if rows == 1:
        pass
    elif coordinate_row == 0 and rows == 1:
        return results
    elif coordinate_row == 0 and rows > 1:
        results.append(array[coordinate_line][coordinate_row + 1])
    elif coordinate_row == rows - 1:
        results.append(array[coordinate_line][coordinate_row - 1])
    else:
        results.append(array[coordinate_line][coordinate_row - 1])
        results.append(array[coordinate_line][coordinate_row + 1])
    return results
 
 
print(*(sorted(get_neighbours(coordinate_line, coordinate_row))))

def merge(arr: list, left: int, mid: int, right: int):
    # Если левая или правая часть пуста, мы имеем дело список
    # единственной частью, которая уже отсортирована.
    if not left:
        return left
    if not right:
        return right

    # Определение переменных для процесса слияния.
    result = []
    leftindex = 0
    rightindex = 0
    totalLen = len(left) + len(right)

    # Работаем, пока не будут объединены все элементы.
    while (len(result) < totalLen):

        # Выполняем сравнения и сливаем части
        # в соответствии со значениями элементов.
        if left[leftindex] < right[rightindex]:
            result.append(left[leftindex])
            leftindex += 1
        else:
            result.append(right[rightindex])
            rightindex += 1
        # Если левая или правая часть длиннее, добавляем
        # оставшиеся элементы к результату.
        if leftindex == len(left) or rightindex == len(right):
            result.extend(left[leftindex:]
            or right[rightindex:])
            break

    return result


def merge_sort(arr: list, left: int, right: int):
    # Проверяем разбит ли список на отдельные части.
    if len(arr) == 1:
        return arr
    # Находим средину списка.
    middle = len(arr)//2

    # Разбиваем список на две части.
    left = merge_sort(arr, 0, arr[:middle])
    right = merge_sort(arr, arr[middle:], len(arr))

    # Объединяем отсортированные части в одну.
    print("Левая часть:", left)
    print("Правая часть:", right)
    merged = merge(left, right)
    print("Объединены в ", merged)
    return merged
    

def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0 , 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected
def merge(array, left, middle, right):
    	# Your code
	# “ヽ(´▽｀)ノ”
	pass
def merge(array, left, middle, right):
    # Если левая или правая часть пуста, мы имеем дело список
    # единственной частью, которая уже отсортирована.
    if not len(left):
        return left
    if not len(right):
        return right

    # Определение переменных для процесса слияния.
    result = []
    leftindex = 0
    rightindex = 0
    totallen = len(left) + len(right)

    # Работаем, пока не будут объединены все элементы.
    while (len(result) < totallen):

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

def merge_sort(array, left, right):
    if len(array) == 1:  # базовый случай рекурсии
        return array

    #  запускаем сортировку рекурсивно на левой половине
    left = merge_sort(array[0: len(array)/2])

    #  запускаем сортировку рекурсивно на правой половине
    right = merge_sort(array[len(array)/2: len(array)])

    #  заводим массив для результата сортировки
    result = [] * len(array)

    #  сливаем результаты
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
    #  выбираем, из какого массива забрать минимальный элемент
    if left[l] <= right[r]:
        result[k] = left[l]
        l += 1
    else:
        result[k] = right[r]
        r += 1
    k += 1

    #  Если один массив закончился раньше, чем второй, то
    #  переносим оставшиеся элементы второго массива в результирующий
    while l < len(left):
        result[k] = left[l]  #  перенеси оставшиеся элементы left в result
            l += 1
            k += 1
    while r < len(right):
        result[k] = right[r]  #  перенеси оставшиеся элементы right в result
            r += 1
            k += 1

        return result


def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0 , 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected
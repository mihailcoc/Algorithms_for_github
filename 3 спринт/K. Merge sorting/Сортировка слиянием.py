def mergesort(list):
    # Проверяем разбит ли список на отдельные части.
    if len(list) < 2:
        return list
    # Находим средину списка.
    middle = len(list)//2

    # Разбиваем список на две части.
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    # Объединяем отсортированные части в одну.
    print("Левая часть:", left)
    print("Правая часть:", right)
    merged = merge(left, right)
    print("Объединены в ", merged)
    return merged


def merge(left, right):
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
    while (len(result)) < totallen):

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

mergesort(data)
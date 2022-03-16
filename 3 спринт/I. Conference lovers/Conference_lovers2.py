def Compare(lhs: str, rhs: str):
    if int(lhs) > int(rhs):
        return True
    return False


def GetTop(array, less):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на компаратор less
        while j > 0 and less(Compare, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
        # return [array[a] for a in array]
    for i in range(1, len(array)):
        array[i]
        #и вот здесь остановился 
    return [array[a] for a in array]
    



if __name__ == '__main__':
    q_of_stud = int(input())
    array = input().split()
    result_q_vuz = int(input())
    result = GetTop(q_of_stud, array, result_q_vuz)
    print(result)

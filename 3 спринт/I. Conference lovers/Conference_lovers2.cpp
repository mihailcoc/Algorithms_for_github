bool Compare(pair <int, int> lhs, pair <int, int> rhs)
    //  Компаратор 
    if (lhs.second == rhs.second)
        return lhs.first < rhs.first
    else
        return lhs.second > rhs.second

array <int> GetTop(array <int> data, int count)
    //  Создаём хеш таблицу и нумеруем её
    hash_table <int, int> counter
    for (val in data)
        counter[val]++
    
    array <pair <int, int>> data == counter
    //  Сортируем с помощью компаратора хеш таблицу
    Sort(data, Compare)

    array <int> result
    // Добавляем в результат количество id университетор по частоте их появления.
    for (int i = 0; i < count; ++i)
        result.Add(data[i])
    return result
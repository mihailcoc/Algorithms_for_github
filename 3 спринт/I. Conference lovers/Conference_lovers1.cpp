array <int> GetTopElements(array <int> values, <int> count)
    hash_table; <int, int> fregency
        for (int val in values)
            fregency[val]++

        array <int>  result
        heap <pair <int, int>> heap
        for (val, freg in fregency)
            heap.Add(freg, val)
            if (heap.Size > fregency.Size - count)
                val, freg = heap.Top
                result.Add(val)
                heap.Pop
        return result
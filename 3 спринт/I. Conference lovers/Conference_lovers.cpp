#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <utility>
​
using namespace std;
​
​
vector<int> getTop(vector<pair<int, int>> data, size_t s_size) {
    sort(data.begin(), data.end(), 
        [](auto lhs, auto rhs) {return lhs.second > rhs.second;});
    vector<int> result;
    for(int i = 0; i < s_size; ++i) {
        result.push_back(data.at(i).first);
    }
    return result;
}
​
​
int main()
{
    // размер выборки из топовых элементов
    size_t size;
    cin >> size;
    
    // сбор первоначальных данных о посетителях
    map<int, int> id_count;
    int id;
    while(cin >> id) {
        ++id_count[id];
    };
    
    // выборка 'size' топовых ВУЗов
    vector<int> top_results = getTop(
        vector<pair<int, int>>(id_count.begin(), id_count.end()), size);
    
    // вывод на печать
    for(auto result : top_results) {
        cout << result << " ";
    }
​
    return 0;
}
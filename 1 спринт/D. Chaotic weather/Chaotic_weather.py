def main(input_ls):
    weather_ls = [int(el) for el in input_ls]
    weather_ls = weather_ls[1:]
    count = 0
                  
    for i in range(1, len(weather_ls)-1):
        if weather_ls[i-1] < weather_ls[i] > weather_ls[i+1]:
                count += 1
    try:
        if weather_ls[1]:
                
            if weather_ls[0] > weather_ls[1]:
                count += 1
            
            if weather_ls[-2] < weather_ls[-1]:
                count += 1
                    
    except Exception:
        count += 1
            
    return count
        
if __name__ == '__main__':
    with open('input.txt') as f:
        input_ls = f.read().split()
        count = main(input_ls)
        print(count)
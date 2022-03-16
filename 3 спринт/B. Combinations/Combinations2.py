keyboard = {
  '1': [],
  '2': ['a','b','c'],
  '3': ['d','e','f'],
  '4': ['g','h','i'],
  '5': ['j','k','l'],
  '6': ['m','n','o'],
  '7': ['p','q','r','s'],
  '8': ['t','u','v'],
  '9': ['w','x','y','z'],
  '0': []
}
 
def printkeys(numbers, prefix=""):
    result = []
 
    if len(numbers) == 0:
        print(prefix)
        return
 
    for letter in keyboard[numbers[0]]:
        printkeys(numbers[1:], prefix+letter)
 
    return result
 
 
 
if __name__ == '__main__':
    numbers = input()
    result = printkeys(numbers)
    print(result)
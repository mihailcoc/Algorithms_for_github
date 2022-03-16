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
 
numbers = input()

result = []

def printkeys(numbers, prefix=""):
    
    if len(numbers)==0:
        result.append(prefix)
        return
 
    for letter in keyboard[numbers[0]]:
        prefix_string = printkeys(numbers[1:], prefix+letter)
        result.append(prefix_string)
    
    return result
 
 
print(printkeys(numbers))
def count_character(string):
    count = 0
    for i in string:
        count += 1
    return count
word = "Hello"
print(word)
print(count_character(word))
a=['h', 'e', 'l', 'l', 'o']
a.remove("l")
print(a)
print("I am poping ", a.pop())
print("I am poping ", a.pop(1))
print(a)
def reverse(lst):
    new = []
    llen = len(lst)
    if llen<2:
        return list
    while llen>0:
        new.append(lst[llen-1])
        llen=llen-1
    return new
def find_max(lst):
    if not (lst):
        return None
    largest = lst[0]
    for value in lst:
        if value > largest:
            largest = value
    return largest
def find_min(lst):
    if not lst:
        return None
    smallest = lst[0]
    for value in lst:
        if value < smallest:
            smallest = value
    return smallest
def find_min_max(lst):
    largest = find_max(lst)
    smallest = find_min(lst)
    return (smallest, largest)
numbers = [3, 1, -4, 1, 5, 9009]
result = reverse(numbers)
print(result)
result = reverse(result)
print(result)
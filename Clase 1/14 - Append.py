numbers = [1,2,3,4,5]

# Append

numbers.append(6)
print(numbers)

# Insert

numbers.insert(1,2)
print(numbers)

# Remove

numbers.remove(2)

print(numbers)

# Pop

deleted_value = numbers.pop()
print(numbers, deleted_value)

# Pop (elimina por indice)

numbers.pop(0)
print(numbers)

# Reverse

numbers.insert(0,1)
print(numbers)

numbers.reverse()
print(numbers)

# Sort

numbers_a = [1,10,8,6,11]
# numbers_a.sort(reverse=True)
numbers_a.sort()
print(numbers_a)

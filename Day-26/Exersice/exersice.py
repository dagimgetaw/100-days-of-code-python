numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n**2 for n in numbers]
print(squared_numbers)

even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)


with open('file1.txt') as file1:
    content1 = file1.read().split()
with open('file2.txt') as file2:
    content2 = file2.read().split()

arr = [int(num) for num in content1 if num in content2]

print(arr)

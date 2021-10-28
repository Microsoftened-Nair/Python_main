dict = {}

n = int(input('Enter the number of key-value pairs in the dictionary: '))

for i in range(1, n+1):
    a = input('Enter key: ')
    b = int(input('Enter a numerical value: '))
    dict[a]=b

ans = 1

for j in dict:
    ans = ans * dict[j]

print('The product of the values is: ', ans)

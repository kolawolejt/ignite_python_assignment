# Q1a
print ('Q1a')
for k in range(2,41,2):
    print(k)

print(' ')
# Q1b
print ('Q1b')
j=1
while j<41:
    print(j)
    j=j+2

print('...')
print(' ')
# Q2
print ('Q2')
list = (3,7,3,9,10,25)
product = 1
for l in range(0,6):
    product = product*list[l]
print(product)

print('...')
print(' ')
# Q3
print ('Q3')
print('Hello, please enter a number to have its times table.')
number = int(input())
for i in range(0,13):
    product1 = number*i
    print(number, 'x', i, '=', product1)

print('...')
print(' ')
# Q4
print('Q4')
for m in range(100,0,-4):
    print(m)

print('...')
print(' ')
# Q5
print('Q5')
print('Please enter your name')
name = input()
for n in range(0,len(name)):
    print(name[n])

print(' ')
# Q5b
print('Q5b')
for n in range(0,len(name)):
    print('Character', n+1, ':', name[n])
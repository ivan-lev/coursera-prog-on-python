import sys
num_steps = int(sys.argv[1])
result = ''
k = 1

while k <= num_steps:
    result = ' ' * (num_steps - k) + '#' * k
    k += 1
    print(result)

#for i in range(num_steps):
#    print(' ' * (num_steps - i - 1), '#' * (i + 1), sep = '')

total = 0

with open('basic_math_more.txt', 'r') as inp, open('flag.txt', 'w') as outp:
   for line in inp:
       try:
           num = long(line)
           total += num
           outp.write(line)
       except ValueError:
           print('{} is not a number!'.format(line))

print('Total of all numbers: {}'.format(total))
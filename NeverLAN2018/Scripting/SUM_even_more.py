import re

with open('even_more_numbers_with_junks.txt') as f:
    print(sum(long(i) for i in re.findall(r'\b\d+\b', f.read())))

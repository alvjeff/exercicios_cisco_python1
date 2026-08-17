#operadores bit a bit

from time import process_time_ns


i = 15
j = 22

log = i and j
print(log)

bit = i & j
print(bit)

logneg = not i
print(logneg)

bitneg = ~i
print(bitneg)

print(i & j)
print(i | j)
print(i ^ j)
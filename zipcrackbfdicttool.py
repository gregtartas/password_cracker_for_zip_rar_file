import itertools

c = raw_input ("enter: ")
x = raw_input ("max l: ")

file2 = open ("dictionary.txt", 'w')

res = itertools.product(c,repeat=int(x))
for i in res:
    file2.write("\n" +''.join(i))
file2.close()
        

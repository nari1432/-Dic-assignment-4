#10.Write a Python script to merge two Python dictionaries.d

d1 = {'a':10, 'b':20, 'c':30}
d2 = {'a':40, 'd':60, 'e':70}

dict=d1.copy()

dict.update(d2)

print(dict)
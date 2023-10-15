#script to check whether a given key already exists in a dictionary.

d = {1:12, 2:13, 3:44, 4:55, 5:77, 6:88}
def is_key_present(x):
    if x in d:
        print('key is present in the dictionary')

    else:
        print('key not  present in the dictionary')

is_key_present(5)
is_key_present(9)

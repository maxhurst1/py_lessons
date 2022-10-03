string_list = ["a", "b", "c", "d", "e"]
ints_list = [1, 2, 3, 4, 5]

def reverse_list(l):
    l.reverse()

def concatenate_lists(list_one, list_two):
    for el in list_two:
        list_one.append(el)

def list_num_square(l):
    for i in range(len(l)):
        l[i] = l[i] * l[i]

def list_zip(list_one, list_two):
    return list(zip(list_one, list_two))

reverse_list(ints_list)
list_num_square(ints_list)
concatenate_lists(string_list, ints_list)
print(string_list)

# Zips both of the lists together
print(list_zip(string_list, ints_list))

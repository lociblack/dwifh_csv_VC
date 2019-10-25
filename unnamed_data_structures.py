from random import choice

def recieve_multiple(*stuff):
    for val in stuff:
        print(val)

my_list = ['apples', 'oranges', 'prunes']

return_multiple(*my_list)

# basic example
def dict_builder_simple(**kwargs):
    return kwargs           # this is literally the parameter


# example in which parameter library is used inside body of function
def dict_builder(**kwargs):
    my_dict = kwargs    # we store kwargs in a dict
    my_dict['One More'] = 350  # we add another item to that dict
    return kwargs


x = dict_builder(Name = 'Johnny', Film = 'The Shining')
print(x)


m = ['Name', 'Color', 'City']

p = ['Michael', 'Blue', 'Portland']

def dict_builder_two(key_list, value_list):
    my_dict = {}
    for key, val in zip(key_list, value_list):
        my_dict[key] = val
    return my_dict

d = dict_builder_two(m, p)
print(d)


list_of_dicts = []
the_keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
stuff = ['Tree', 'House', 'Camera', 'Film', 'TV', 'Food', 'Animal', 'Sea']

count = 1
for x in range(3):
    d = dict_builder_two(m, p)  # we assign the returned dict to name 'd'
    list_of_dicts.append(d) # we append 'd' to the dictionary list
    # but it doesn't show up as 'd', it shows up as the contents of the list.
    # you aren't appending the 'name', d; you are appending the value (object)
    # in memory that d references.

print(list_of_dicts)








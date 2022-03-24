from functools import singledispatch

strs = """id 13
        first_name Dinesh
        last_name Zero
        is_user True
        roll_num 114"""

my_dict = dict(x.split() for x in strs.splitlines())
meta_dict = {'id': int, 'first_name': str, 'last_name': str, 'is_user': bool, 'roll_num': int}
new_dict = {k: meta_dict.get(k, str)(v) for k, v in my_dict.items()}
print(new_dict)


@singledispatch
def fprint(data):
    print(f'({type(data).__name__}) {data}')


@fprint.register(dict)
def _(data):
    formatted_header = f'{type(data).__name__} -> key : value'
    print(formatted_header)
    print('-' * len(formatted_header))
    my_list = []
    for value in data.values():
        if isinstance(value, int) and value != True or False:
            my_list.append(value)

    max_value = max(my_list)
    min_value = min(my_list)

    print('The max value of a integer is:', max_value)
    print('The min value of a integer is:', min_value)

    my_list2 = []

    for value in data.values():
        if isinstance(value, str):
            my_list2.append(value)

    max_len = max(my_list2, key=len)
    min_len = min(my_list2, key=len)

    print('The string with highest length is', max_len)
    print('The string with lowest length is', min_len)

    for value in data.values():
        if isinstance(value, bool):
            print('The boolean value in the dictionary is:', value)


fprint(new_dict)

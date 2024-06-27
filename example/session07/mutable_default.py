def put_value_in_list(value: int, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


print(put_value_in_list(value=1))
print(put_value_in_list(value=2))
print(put_value_in_list(value=3))
print(put_value_in_list(value=4))
print(put_value_in_list(value=5))

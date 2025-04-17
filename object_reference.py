new_list = [1, 2, 3]
same_list = new_list

print(*same_list)
same_list[0] = 3

#refer to the same object

print(*new_list)

new_string = 'Hello'
same_string = new_string

print(same_string)
same_string = 'World'

print(new_string)
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 5:
        print("It's 5!")
        break
else:
    print('5 was not listed')  

new_list = [6, 7, 8, 3]

total = 0

new_list = [6, 7, 8, 3]

total = 0
index = 0

while index < len(new_list):
    num = new_list[index]
    if num == 3:
        total += num
    index += 1
else:
    print(f"Now it equals to {total}")



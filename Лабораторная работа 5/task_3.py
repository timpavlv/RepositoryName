from random import randint

def get_unique_list_numbers() -> list[int]:

 while True:
        num = []
        for i in range(15):
            num.append(randint(-10, 10))
        if len(num) == len(set(num)):
            return num
        else:
            continue

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
#
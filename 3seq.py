import re
n = input('Введите цифры, которые будут в первом списке: ')
result_first = [int(item) for item in re.split(',|/', n)]
n = input('Введите цифры, которые будут во втором списке: ')
result_second = [int(item) for item in re.split(',|/', n)]
#нужно делать копию списка, тк при удалении один элемент проскакивает
for item in result_first[:]:
    if item in result_second:
        result_first.remove(item)
print(result_first)
import re
n = input('Введите цифры, которые будут в списке: ')
result = [int(item) for item in re.split(',|/', n)]
res_list = []
for item in result:
    if item not in res_list:#if result.count(item) == 1
        res_list.append(item)

print(res_list)
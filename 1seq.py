n = int(input('Введите количество элементов будущего списка: '))
list_people = []
for i in range(n):
   list_people.append(int(input('Введите элемент {}: '.format(i+1))))
print(sorted(list_people))
set1 = {1, 4, 5, 4, 2, 7}
set2 = {2,7, 8, 0, 9}

print(set1)
print(set2)

print(f'Sum of the sets: {(set1 | set2)}')
print(f'Intersection of the sets: {(set1 & set2)}')
print(f'Difference of the sets: {(set1 - set2)}')
print(f'Symetric difference of the sets: {(set1 ^ set2)}')


list_of_numbers = [1, 2, 3, 4, 5, 6, 1, 3, 5, 6,]
list_without_duplicates = list(set(list_of_numbers))
print(list_without_duplicates)

names = {'Kamil', 'ALeksandra', 'Oliwia', 'Patryk', 'Szymon'}
list_of_names = list(names)
list_of_male_names = []
list_of_female_names = []

for name in list_of_names:
    if name[-1] == 'a':
        list_of_female_names.append(name)
    else:
        list_of_male_names.append(name)

print(list_of_male_names)
print(list_of_female_names)

male_names = set()
female_names = set()

for name in names:
    if name[-1] == 'a':
        female_names.add(name)
    male_names = names - female_names


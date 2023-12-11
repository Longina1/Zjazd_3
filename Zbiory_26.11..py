NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
centrum = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
krzyki = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

#ile osób chorowało w ostatnim roku w centrum
print(f'Number of sick people living in centre in the last year: {len(chorzy_rok & centrum)}.')

#
print(f'Number of sick people living in centre in the last year: {len(centrum & chorzy_rok)}.')


for item in chorzy_miesiac:
    if item in chorzy_rok:
        print((f'People sick last month and last year: {item}.'))

print(f'People sick during the last month and not sick during the last year: {chorzy_miesiac - chorzy_rok}')
print(len(chorzy_miesiac - chorzy_rok))

duplicates = centrum & krzyki
print(duplicates)

if len(centrum & krzyki) > 0:
    decision = input('From which folder duplicates should be deleted? K/C ')
    if decision.upper() == 'C':
        centrum = centrum - (centrum & krzyki)
    elif decision.upper() == 'K':
        krzyki -= centrum
    else:
        for pesel in centrum & krzyki:
            centrum.remove(pesel)

print(centrum)
print(f'Deduplicated centre list: {centrum - (centrum & krzyki)}')

#zddrowy, chory z krzyków, centrum, powinien być w NFZ

for pesel in krzyki | centrum | chorzy_rok | chorzy_miesiac:
    if pesel not in NFZ:
        print(NFZ)
        print(pesel)
        NFZ.add(pesel)
        print(NFZ)

all = chorzy_rok | chorzy_miesiac | centrum | krzyki
NFZ |= all

#żeńskie parzyste
NFZ_men = set()
NFZ_women = set()
for pesel in NFZ:
    if pesel % 2 == 0:
        NFZ_women.add(pesel)
NFZ_men = NFZ - NFZ_women

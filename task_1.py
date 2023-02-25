stix = input()
glasn = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
stix = stix.lower().split()
sum = list()
for item in stix:
    k = 0
    for letter in item:
        if letter in glasn:
            k += 1
    sum.append(k)
print(sum)
for i in range(len(sum)):
    if sum[i-1] != sum[i]:
        print('Пам парам')
        break
    else:
        print('Парам пам-пам')
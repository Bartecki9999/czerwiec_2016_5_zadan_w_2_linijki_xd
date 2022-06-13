a, b, c, d, e, f = open('liczby.txt', 'r'), open('liczby.txt', 'r'), open('liczby.txt', 'r'), open('liczby.txt', 'r'), open('liczby.txt', 'r'), open('liczby.txt', 'r')
print(len([1 for i in a if i.strip()[-1] == '8']), len([1 for i in b if i.strip()[-1] == '4' and '0' not in i.strip()]), len([1 for i in c if i.strip()[-1] == '2' and int(i.strip()[:-1], 2) % 2 == 0]), sum([int(i.strip()[:-1], 8) for i in d if i.strip()[-1] == '8']), max([int(i.strip()[:-1], int(i.strip()[-1])) for i in e]), min([int(i.strip()[:-1], int(i.strip()[-1])) for i in f]))


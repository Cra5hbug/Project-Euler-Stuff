results = []
with open('ProjectEuler13.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split(','))


count = 0
for i in results:
    count += int(i[0])
print(str(count)[:10])

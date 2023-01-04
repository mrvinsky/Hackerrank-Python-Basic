records = []

for _ in range(int(input())):
    name = input()
    score = float(input())

    records.append([name, score])
names = sorted([n[0] for n in records if n[1] == sorted(set([records[i][1] for i in range(len(records))]))[1] ])
for i in names: print(i)
lis = [1,2,1,3,2]
tracker = {}

for i in range(len(lis)):
    if lis[i] in tracker:
        tracker[lis[i]] += 1
    else:
        tracker[lis[i]] = 1

print(tracker)
lis = []
for i in tracker:
    lis.append(i)

print(lis)
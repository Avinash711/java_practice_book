lis = [1,2,99,1,1,2,1, 100, 99, 101, 101]

visited = -1
fr = [0]*len(lis)

for ind in range(len(lis)-1):
    count = 1
    for ind2 in range(ind+1,len(lis)):
        if lis[ind] == lis[ind2]:
            count += 1
            fr[ind2] = visited
    if fr[ind] != visited:
        fr[ind] = count
print('------------------------------')
print('Element      |     Frequency')
print('-------------------------------')
for i in range(len(fr)):
    if fr[i] != visited:
        print (f'Element: {lis[i]}   |   occurred {fr[i]} times.')

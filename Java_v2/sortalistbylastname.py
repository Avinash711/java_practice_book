lis = ['Avinash Gaurav',
       'Surya Chandra', 
       'R Raghvan', 'Sachin Tendulkar']

lis.sort()
print(lis)

lis = sorted(lis, key=lambda x: x.split(' ')[-1])
print(lis)
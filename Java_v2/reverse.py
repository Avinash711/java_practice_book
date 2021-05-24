class Reverse:
    def __init__(self, lis):
        self.lis = lis

    def reverse(self):
        print(f'Reversed lis is: {self.lis[::-1]}')

        for i in range(1,len(self.lis)+1):
            print(self.lis[-i], end= " ")

if __name__ == '__main__':
    obj = Reverse([1,2,3,4,5])
    obj.reverse()
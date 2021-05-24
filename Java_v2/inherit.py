class Animal:
    def __init__(self):
        print(f'This is Animal Class!!')
    def display(self):
        print(f'Animal have life!!')

class Lion(Animal):
    def __init__(self):
        super().__init__()
        print(f'This is Lion Class!!')

    def display(self):
        super().display()
        print(f'Lion is the king of Jungle')


if __name__ == '__main__':
    lion = Lion()
    lion.display()
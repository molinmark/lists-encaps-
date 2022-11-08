import random
class lists():
    def __init__(self):
        self.__list0 = []
        self.__list1 = []
        self.__list2 = []
        self.__n = random.randint(6, 20)

    @property
    def list0(self):
        return self.__list0

    @property
    def list1(self):
        return self.__list1

    @property
    def list2(self):
        return self.__list2

    def create_list_0(self):
        for i in range(self.__n):
            k = random.randint(1, 100)
            self.__list0.append(k)

    def create_list_1(self):
        for i in range(2, self.__n, 3):
            self.__list1.append(self.__list0[i])

    def create_list_2(self):
        for i in range(self.__n-1, -1,-1):
            self.__list2.append(self.__list0[i])

def main():
    l=lists()
    l.create_list_0()
    l.create_list_1()
    l.create_list_2()
    print('Сгенерированная последовательность:',l.list0)
    print('Каждый 3 элимент:',l.list1)
    print('Обратная последовательность:',l.list2)

main()

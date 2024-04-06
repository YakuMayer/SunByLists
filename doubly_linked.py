from singly_linked import *


class Doubly_Object():
    def __init__(self, value, link1, link2):
        self.value = value
        self.link1 = link1
        self.link2 = link2
        self.linkSL = Singly_Linked()


class Doubly_Linked():
    def __init__(self):
        self.head = None
        self.counter = 0

    def add_element(self, elem):
        obj = self.head
        if self.head:
            while True:
                if obj.link2 == self.head or obj.link2 == None:
                    obj.link2 = Doubly_Object(elem, obj, self.head)
                    self.head.link1 = obj.link2
                    break
                else:
                    obj = obj.link2

        else:
            self.head = Doubly_Object(elem, None, None)

    def print_list(self):
        if self.head:
            obj = self.head
            while True:
                print(f"{obj.value} - {obj.linkSL.singly_print_list()}")
                if obj.link2 == self.head or obj.link2 == None:
                    break
                else:
                    obj = obj.link2
            print("")
        else:
            print("Список пуст")

    def search_element(self, elem, word):
        alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        if self.head:
            obj = self.head
            if (alf.find(elem) > self.counter and alf.find(elem) - self.counter < self.counter + len(alf) - alf.find(
                    elem)) or (alf.find(elem) < self.counter and self.counter - alf.find(elem) > self.counter + len(
                alf) - alf.find(elem)):
                while True:
                    if elem == obj.value:
                        obj.linkSL.singly_add_element(word)
                        break
                    else:
                        if obj.link2 == self.head or obj.link2 == None:
                            print("Такого элемента в списке нет")
                            break
                        else:
                            obj = obj.link2
                            self.counter += 1
            elif (alf.find(elem) < self.counter and self.counter - alf.find(elem) < alf.find(elem) + len(
                    alf) - self.counter) or (
                    alf.find(elem) > self.counter and self.counter - alf.find(elem) > alf.find(elem) + len(
                    alf) - self.counter):
                while True:
                    if elem == obj.value:
                        obj.linkSL.singly_add_element(word)
                        break
                    else:
                        if obj.link1 == self.head or obj.link1 == None:
                            print("Такого элемента в списке нет")
                            break
                        else:
                            obj = obj.link1
                            self.counter -= 1
            else:
                print("Я запутался")
        else:
            print("Список пуст")
        if self.counter < 0:
            self.counter = len(alf) + self.counter
        elif self.counter > len(alf):
            self.counter = self.counter % len(alf)

def main():
    DL = Doubly_Linked()
    DL.add_element("а")
    DL.print_list()
if __name__ == "__main__":
    main()

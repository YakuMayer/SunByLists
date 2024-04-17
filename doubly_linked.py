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
        self.last = self.head

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
            self.last = self.head

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

    def move_tracker(self, elem, word, obj, direct = True):
        alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        while True:
            if elem == obj.value:
                obj.linkSL.singly_add_element(word)
                self.last = obj
                break
            else:
                if elem not in list(alf):
                    print("Возможно в тексте есть иностранный алфавит")
                    break
                else:
                    if direct:
                        obj = obj.link2
                        self.counter += 1
                    else:
                        obj = obj.link1
                        self.counter -= 1

    def search_element(self, elem, word):
        alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        direct_distance = abs(alf.find(elem) - self.counter)
        reverse_distance = len(alf) - direct_distance
        if self.last:
            obj = self.last
            if (self.counter > alf.find(elem) and direct_distance < reverse_distance) or (
                    self.counter < alf.find(elem) and direct_distance > reverse_distance):
                self.move_tracker(elem, word, obj, direct=True)
            elif (self.counter > alf.find(elem) and direct_distance > reverse_distance) or (
                    self.counter < alf.find(elem) and direct_distance < reverse_distance):
                self.move_tracker(elem, word, obj, direct=False)
            elif alf.find(elem) == self.counter:
                obj.linkSL.singly_add_element(word)
                self.last = obj
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

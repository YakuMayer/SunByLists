class Singly_Object():
    def __init__(self, value, link):
        self.value = value
        self.link = link

class Singly_Linked():
    def __init__(self):
        self.head = None

    def singly_add_element(self, elem):
        obj = self.head
        if self.head:
            while True:
                if obj.link:
                    obj = obj.link
                else:
                    obj.link = Singly_Object(elem, None)
                    break
        else:
            self.head = Singly_Object(elem, None)

    def singly_print_list(self):
        ans = ""
        if self.head:
            obj = self.head
            while True:
                ans += f"{obj.value} | "
                if obj.link:
                    obj = obj.link
                else:
                    break
            return ans
        else:
            return "Список пуст"

    def search_element(self, elem):
        if self.head:
            obj = self.head
            while True:
                if elem == obj.value:
                    print("Элемент найден")
                    break
                else:
                    if obj.link:
                        obj = obj.link
                    else:
                        print("Такого элемента в списке нет")
                        break
        else:
            print("Список пуст")

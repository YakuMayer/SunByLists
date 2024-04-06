from doubly_linked import *
DL = Doubly_Linked()
with open("text.txt", "r", encoding="utf-8") as f:
    text = "".join(e.lower() for e in f.readline() if e.isalnum() or e == " ").split()

alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

for i in alf:
    DL.add_element(i)

DL.print_list()

for j in text:
    print(j)
    DL.search_element(j[0], j)
#
DL.print_list()

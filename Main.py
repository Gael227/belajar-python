toDoList = []
def addList():
    while True:
        isi = input("Add to list: ")
        if isi.lower() == "stop":
            break
    toDoList.append(isi)

print('-------todo list--------')
print('1. add to list')
print('2. delete item in list')
print('3. show list')
print('4. keluar')

inp = int(input(print('choose one option: ')))

if inp == 1:
    addList()
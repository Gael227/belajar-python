#array kosong yg akan diisi di function addList
toDoList = []

#function untuk memasukkan input user ke dalam array toDoList
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

#variabel yg menyimpan hasil input user
inp = int(input('choose one option: '))

#percabangan berdasarkan input user
if inp == 1:
    addList()